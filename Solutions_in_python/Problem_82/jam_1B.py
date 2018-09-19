#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wani
#
# Created:     21/05/2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys

def fullpattern(end):
    ls = []
    for i in range(end):
        l = [i]
        ls.append(l)
        for j in range(i+1,end):
            l = l + [j]
            ls.append(l)
    return ls

def gettime(cs,dis,ini):
    pats = fullpattern(cs)
    maxtime = 0
    for pat in pats:
        num = 0
        max,min = ini[pat[0]][0],ini[pat[0]][0]
        for i in pat:
            num += ini[i][1]
            if ini[i][0] > max:
                max = ini[i][0]
            if ini[i][0] < min:
                min = ini[i][0]
        mov = (num-1)*dis - (max -min)
#        print mov,pat,num,max,min
        if mov > 0:
            time = mov / 2.0
            if time > maxtime:
                maxtime = time
    return maxtime

def main():
    input = sys.argv[1]
    output = sys.argv[2]

    f = open(input)
    fo = open(output,"w")
    cases = int(f.readline().strip())
    for i in range(cases):
        outs = []
        ini = []
        l = f.readline().strip().split()
        cs,dis = int(l[0]),int(l[1])
        for c in range(cs):
            l = f.readline().strip().split()
            ponit,venders = int(l[0]),int(l[1])
            ini.append([ponit,venders])
        outs.append("Case #%d: "%(i+1)+str(gettime(cs,dis,ini))+"\n")
        for out in outs:
            print out,
            fo.write(out)
    fo.close()
    f.close()

if __name__ == '__main__':
    main()