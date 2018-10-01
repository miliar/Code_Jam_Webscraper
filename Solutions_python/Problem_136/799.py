#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      kiit
#
# Created:     10/04/2014
# Copyright:   (c) kiit 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def list_int():
    m=raw_input()
    m=m.split()
    m= map(float,m)
    return m

def main():

    d=[]
    t=int (input())
    for i in range(t):
        m=list_int()
        [c,f,x]=m
        cover=0
        n=float(x/2)
        rate=2
        time=0.0
        temp=0.0
        while(cover<x):
            time=(c/rate)
            rate=rate+f
            temp=time+(x/rate)
            cover =x
            if (temp<n):
                while (temp<n ):
                    n=temp
                    time=time +(c/rate)
                    rate= rate+f
                    temp=time+(x/rate)

        print 'Case #'+str(i+1)+': '+ str(n)






if __name__ == '__main__':
    main()
