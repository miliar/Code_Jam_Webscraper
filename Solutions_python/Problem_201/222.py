# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math

f = open("C-large.in",'r')
g = open("Answer.txt", 'w')

def calcuate_priority(i, j):
    if (i-j)%2 == 0:
        return (i+j-1)/2, ((j-i)/2 - 1,(j-i)/2 - 1, (i+j)/2)
    else:
        return (i+j-1)/2, ((j-i-1)/2 - 1, (j-i+1)/2, (i+j-1)/2)
#end_def

t = int(f.readline())  # read a line with a single integer
for i in range(1, t + 1):
    N, K = f.readline().strip().split(" ")
    N, K = int(N), int(K)
    have = {N:1}
    while K > 0:
        m = max(have.keys())
        count = have[m]
        if K > count:
            K -= count
            have.pop(m, None)
            if m%2 == 1:
                have[(m-1)/2] = have.setdefault((m-1)/2, 0) + 2*count
            else:
                have[m/2 - 1] = have.setdefault(m/2 - 1, 0) + count
                have[m/2] = have.setdefault(m/2, 0) + count
            #end_if
        else:
            K = 0
            if m%2 == 1:
                g.write("Case #{}: {} {}\n".format(i, (m-1)/2, (m-1)/2))
            else:
                g.write("Case #{}: {} {}\n".format(i, m/2, m/2 - 1))
            #end_if
    #end_w
#end_for
