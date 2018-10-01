# file = open('b.in', 'r') # r for read
# file = open('B-small-attempt1.in', 'r') # r for read
file = open('B-large.in', 'r') # r for read
out = open('b.out', 'w') # w for write
#
n = int(file.readline().strip()) 
for c in range(n):
    out.write('Case #{}: '.format(1+c))
    l = file.readline().strip()
    maxs = []
    m = '0'
    for e in l:
        maxs.append(m)
        if e > m:
            m = e
    # print(l)
    # print(maxs)
    # print()
    for i in range(len(l)-1, 0, -1):
        if l[i] < maxs[i]:
            l = l[:i-1] + chr(ord(l[i-1]) -1) + '9'*(len(l) - i)
            # print(l)#, ('b' if i+1 == len(l) else l[i+1]))
    out.write( str( int(l)) + '\n' )
#
file.close()
out.close()