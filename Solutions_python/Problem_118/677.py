def isPalindrome(number):
    strNum = str(number)
    for i in range(len(strNum)/2 + 1):
        if strNum[i] != strNum[-1*(i+1)]:
            return False
    return True
'''
for i in range(100000000):
    if isPalindrome(i) and isPalindrome(i*i):
        print i*i
'''


filename = "C-large-1.in"
outputname = filename + "out.txt"

inFile = open(filename, 'r')
outFile = open(outputname, 'w')


fairAndSquareNums = [1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004]


def binary_search(seq, t):
    min = 0; max = len(seq) - 1
    while 1:
        if max < min:
            return min
        m = (min + max) / 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m

numTests = int(inFile.readline())

    

for i in range(numTests):
    line = inFile.readline().split()
    count = 0
    indexA = binary_search(fairAndSquareNums, int(line[0]))
    indexB = binary_search(fairAndSquareNums, int(line[1])+1)
    count = indexB-indexA
    outFile.write("Case #" + str(i+1) + ": " + str(count) + '\n')
    print "Case #" + str(i+1) + ": " + str(count)

inFile.close()
outFile.close()

