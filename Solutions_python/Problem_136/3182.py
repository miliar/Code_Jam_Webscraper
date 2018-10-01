__author__ = 'Ana'

import sys

def main():
    file=sys.stdin
    t=int(file.readline())
    for i in range(t):
        line=file.readline()
        values=line.split(' ')
        c,f,x=float(values[0]),float(values[1]),float(values[2])
        time_to_build=0
        ans=x/2
        for j in range(1,int(x),1):
            time_to_build+=c/((j-1)*f+2)
            tmp=time_to_build+x/(j*f+2)
            if tmp<ans:
                ans=tmp
        print 'Case #'+str(i+1)+': '+str(ans)


main()
