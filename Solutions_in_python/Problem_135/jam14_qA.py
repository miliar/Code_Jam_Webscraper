#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      wani
#
# Created:     14/04/2012
# Copyright:   (c) wani 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import copy

def detercards(c1,c2,sq1,sq2):
    ans = sq1[c1-1] & sq2[c2-1]
    if len(ans) == 0:
        return "Volunteer cheated!"
    elif len(ans) == 1:
        for a in ans:
            return str(a)
    else:
        return "Bad magician!"

def main():
    Pname = "jam14qA"
    f = open(r"data/"+Pname+"-input2.txt")
    fo = open(r"data/"+Pname+"-output2.txt","w")

    cases = int(f.readline().strip())
    for i in range(cases):
        choose1 = int(f.readline().strip())
        sq11 = set([int(x) for x in f.readline().strip().split()])
        sq12 = set([int(x) for x in f.readline().strip().split()])
        sq13 = set([int(x) for x in f.readline().strip().split()])
        sq14 = set([int(x) for x in f.readline().strip().split()])
        sq1 = [sq11,sq12,sq13,sq14]
        choose2 = int(f.readline().strip())
        sq21 = set([int(x) for x in f.readline().strip().split()])
        sq22 = set([int(x) for x in f.readline().strip().split()])
        sq23 = set([int(x) for x in f.readline().strip().split()])
        sq24 = set([int(x) for x in f.readline().strip().split()])
        sq2 = [sq21,sq22,sq23,sq24]
        out = "Case #%d: %s"%(i+1,detercards(choose1,choose2,sq1,sq2)) + "\n"
        print(out)
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()
