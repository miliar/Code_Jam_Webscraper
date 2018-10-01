# solution for https://code.google.com/codejam/contest/1460488/dashboard#s=p0
import sys

def solve(a, b):
    n = a
    count = 0
    while n <= b:
        digits = [int(d) for d in list(str(n))]
        for l in range(1, len(digits)):
            if sum(digits[:l]) == 0:
                continue
            numList = digits[l:] + digits[:l]
            candidate = int(''.join(map(str,numList)))
            if n < candidate and candidate >= a and candidate <=b:
                count +=1
                #print n, candidate
        n+=1
    return count
    
filename = sys.argv[1] #get filename from arguments
f_in = open(filename,'r')
output = filename.split('.in')[0] + '.out' # generate output filename
f_out = open(output,'w')
n = 0
cases = f_in.readline() #  number of testcases
for n in range(int(cases)):
    line = f_in.readline().rstrip()
    # for each test case do the convertion
    numbers =[int(num) for num in line.split(' ')]
    f_out.write('Case #%d: %d\n' %(n+1, solve(numbers[0],numbers[1])))