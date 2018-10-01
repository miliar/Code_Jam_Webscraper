import sys
import string

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

def recycles(n,B):
    s = str(n)
    digits = len(s)
    ss = s + s
    count = 0
    recycled = set()
    for i in range(1,digits):
        if s[i] == '0':
            continue
        m = eval(ss[i:i+digits])
        if n < m and m <= B:
            recycled.add(m)
    return len(recycled)

if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for x in range(T):
            P = map(int, f.readline().split(' '))
            A = P[0] # first in range
            B = P[1] # last in range
            count = 0
            for n in range(A,B):
                count = count + recycles(n,B)
            outf.write('Case #{0}: '.format(x+1))
            outf.write(str(count))
            outf.write('\n')
