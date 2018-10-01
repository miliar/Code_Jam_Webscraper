from collections import defaultdict
infile = open("C-small-attempt0.in")
outfile = open("C-small-attempt0.out", "w")

lines = infile.readlines()

def rotate(word):
    return word[-1] + word[:-1]
    
def solve(line):
    words = defaultdict(set)
    a, b = line.split()
    ans = 0
    for i in range(int(a), int(b)):
        digits = str(i)
        tdigits = digits

        for j in range(len(digits)-1):
            tdigits = rotate(tdigits)
            if tdigits == digits: continue
            if tdigits not in words[digits] \
                and digits not in words[tdigits] \
                and tdigits[0] != '0' \
                and int(a) <= int(tdigits) <= int(b):
                ans+=1
                #print digits, tdigits

            words[digits].add(tdigits)
            words[tdigits].add(digits)
                
    return str(ans)

for i, line in enumerate(lines[1:]):
    outfile.write("Case #{}: ".format(i+1) + solve(line) + '\n')

outfile.close()
