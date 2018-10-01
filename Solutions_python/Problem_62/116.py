#! /usr/bin/python

#  (c) 2010 Wott (http://wott.net.ru/ , wott@gmail.com)

__author__="Wott"
__date__ ="$23.05.2010 13:05:47$"

import sys

def case(N,m):
    ret = 0
    #print ([[(i[0]>j[0] and i[1]<j[1]) or (i[0]<j[0] and i[1]>j[1]) for i in m] for j in m])
    return (sum([sum([1 if (i[0]-j[0])*(i[1]-j[1])<0 else 0 for i in m]) for j in m])/2)
    for i in range(N):
        for j in range(N):
            if (m[i][0]>m[j][0] and m[i][1]<m[j][1]) or (m[i][0]<m[j][0] and m[i][1]>m[j][1]): ret+=1;
    ret=ret//2
    print("LINE: %d,%s => %d" % (N,m,ret))
    return(ret)

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: %s in.file out.file" % sys.argv[0])
        return
    with open(args[0]) as infile:
        with open(args[1],'w') as outfile:
            T = int(infile.readline())
            for t in range(T):
                N=int(infile.readline().rstrip())
                m = [[int(i) for i in infile.readline().rstrip().split()] for n in range(N)]
                c = case(N,m)
                outfile.write("Case #%d: %d\n" % (t+1,c))

if __name__ == '__main__':
    main()
