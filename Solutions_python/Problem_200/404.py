import sys
#import math

with open(sys.argv[1]) as infile:
    input = infile.readlines()

T = int(input[0])

result = []

def solve_tidy(N):
    instring = str(N)
    n = len(instring)

    outstring = ''
    for i in range(n):
        outcand = outstring + (n - i) * instring[i]
        if int(outcand) <= N:
            outstring += instring[i]
        else:
            outstring += str(int(instring[i]) - 1)
            outstring += (n - len(outstring)) * '9'
            return int(outstring)
    return int(outstring)

for line in input[1:]:
    N = int(line)
    result.append(solve_tidy(N))

with open(sys.argv[1].split('.')[0] + '.out', 'w') as outfile:
    for i, r in enumerate(result):
        outfile.write("Case #%s: %s \n" % (i + 1, r))
