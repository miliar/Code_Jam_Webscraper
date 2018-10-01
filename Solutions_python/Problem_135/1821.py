#!\bin\python
#encoding UTF-8
#solution.py

import sys
import string
import linecache

inname = "A-small-attempt1.in"
outname = "A-small-attempt1.out"
fin = open(inname, "r")
fout = open(outname, "w")

allCaseNum = int(linecache.getline(inname, 1).rstrip("\n"))
caseNum = 0
line = 2

for caseNum in xrange(1, allCaseNum+1):
    first = linecache.getline(inname, line+10*(caseNum-1)+int(linecache.getline(inname,line+10*(caseNum-1)).rstrip("\n"))).rstrip("\n").split( )
    second = linecache.getline(inname, line+10*(caseNum-1)+5 + int(linecache.getline(inname,line+10*(caseNum-1)+5).rstrip("\n"))).rstrip("\n").split( )
    match = [i for i in first if i in second]
    if len(match) == 1:
        answer = "Case #%s: %s\n" %(caseNum, match[0])
    if len(match) >= 2:
        answer = "Case #%s: Bad magician!\n" %(caseNum)
    if len(match) == 0:
        answer = "Case #%s: Volunteer cheated!\n" %(caseNum)
    fout.write(answer)
fin.close()
fout.close()