#!/usr/bin/env python
infile = "C-small-attempt0.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    R, k, N = [int(value) for value in fsrc.readline().split()]
    g = [int(value) for value in fsrc.readline().split()]
    res = "Case #%s: " %(t+1, ) 
    
    euros = 0
    index = 0
    for r in range(R):
        sum = 0
        if index == N: index = 0
        line = 0
        while (sum+g[index]) <= k:
            sum += g[index]
            index += 1
            line += 1
            if line == N: break
            if index == N: index = 0
        euros += sum
            
            
    res += str(euros)
    
    res += '\n'
    print res
    fres.write(res)

fsrc.close()
fres.close()