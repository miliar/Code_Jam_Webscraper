in_file = input('IN: ')
f = open(in_file, 'r')
out = open('out.txt', 'w')

cases = int(f.readline())

for i in range(cases):

    line = f.readline()
    res = line.split()

    z = int(res[0])

    if z == 0:
        out.write("Case #%d: 0\n" % (i + 1))
        continue
    
    needed = 0
    standing = 0
        
    for j in range(z + 1):

        curr = int(res[1][j])

        if curr != 0 and standing < j:
            needed += j - standing
            standing += needed
            
        standing += curr
            
    out.write(("Case #%d: " % (i + 1)) + str(needed) + '\n')
    
f.close()
out.close()
