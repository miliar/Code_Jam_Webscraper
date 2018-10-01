import sys
import re

infile = sys.stdin.readlines()
(L, D, N) = [int(x) for x in infile[0].split()]

outfile = open("out.txt", "w")

for i in range(N):
    count = 0
    restr = "^" + infile[i+D+1].replace("(","[").replace(")","]") +"$"
    reobj = re.compile(restr);
    for j in range(1, D+1):
        if reobj.match(infile[j]):
            count = count + 1
    outfile.write("Case #%d: %d\n"%(i+1, count))

outfile.close()
            
    
    
