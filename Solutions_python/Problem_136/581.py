import sys

args = sys.argv

if len(args) < 2:
    print 'small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

def float_row():
    return map(float, raw_input().split())

# No change before this

def solve():
    C, F, X = float_row()
    r = 2.0
    T = 0
    while X > 0:
        t1 = X/r
        t2 = X/(r+F) + C/r
#        print '-----------'
#        print X, C, r
#        print t1, t2
#        print '-----------'
        if t1 <= t2:
            T += t1
            break
        else:
            T += C/r
            r += F
    return str(T)

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')
# No change after this

out.close()
