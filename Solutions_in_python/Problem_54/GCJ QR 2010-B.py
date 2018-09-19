import sys

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

inFile = open("B-large.in","r")
#inFile = open("test.txt", "r")
outFile = open("large.out", "w")
records = inFile.readlines();

c = 1
seek = 1
t = int(records[0])

while t > 0:
    aLine = records[seek].split()
    n = int(aLine[0])

    nums = []
    for i in range(n):
        nums.append(int(aLine[i+1]))
    nums.sort()

    nums1 = []
    for i in range(n-1):
        nums1.append(nums[i+1]-nums[i])
    nums1.append(nums[n-1]-nums[0])

    print nums
    print nums1
    
    gcd = nums1[0]
    i = 1
    while i < n:
        gcd = GCD(gcd, nums1[i])
        i = i + 1

    print gcd

    temp = nums[0]%gcd
    if temp != 0:
        ans = gcd - temp
    else:
        ans = 0
    outFile.write("Case #" + str(c) + ": " + str(ans) + "\n")
    c = c + 1    
    seek = seek + 1
    t = t - 1

inFile.close()
outFile.close()
