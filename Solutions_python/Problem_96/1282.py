infile = open("B-large.in")
outfile = open("B-large.out", "w")

lines = infile.readlines()

def solve(line):
    ans = 0
    nums = [int(i) for i in line.split()]
    (N, S, p), nums = nums[:3], nums[3:]
    for num in nums:
        i = num/3
        k = num-2*i
        if i >= p or (k >= p and k-i <= 1) or (i+1 >= p and k-i == 2):
            ans+=1
        elif (k >= p and k-i == 2 and S > 0) or (k != 0 and k+1 >= p and k-i == 0 and S > 0):
            ans+=1
            S-=1
    return str(ans)
        

for i, line in enumerate(lines[1:]):
    outfile.write("Case #{}: ".format(i+1) + solve(line) + '\n')

outfile.close()
