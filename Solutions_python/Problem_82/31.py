import sys, time, math

def main(): # gcj 2011 round 1
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    T = int(input())
    for case in range(T):
        cd = input().split()
        C, D = int(cd[0]), int(cd[1])

        p = [ 0 for x in range(C) ]
        num = [ 0 for x in range(C) ]

        for i in range(C):
            pn = input().split()
            p[i], num[i] = int(pn[0]), int(pn[1])
        
        mn = -1
        for i in range(C):
            time = (num[i]-1)*D/2
            if mn<time: mn = time

            total = num[i]
            for j in range(i+1,C,1):
                total += num[j]
                time = ( (total-1)*D-(p[j]-p[i]) )/2
                if mn<time: mn = time
        print("Case #",case+1,": ",mn,sep='',end='\n')
            
        

"""
def main(): # gcj 2011 round 1
    sys.stdin = open("in.txt","r")
    sys.stdout = open("out.txt","w")
    T = int(input())
    for case in range(T):
        N = int(input())
        s = [ 0 for x in range(N) ]
        wp = [ 0 for x in range(N) ]
        owp = [ 0 for x in range(N) ]
        oowp = [ 0 for x in range(N) ]
        for i in range(N):
            s[i] = input()
        #print(s)
        print("Case #",case+1,": ",sep='',end='\n')
        for i in range(N):
            total, win = 0, 0
            for j in range(N):
                if s[i][j]!='.': total += 1
                if s[i][j]=='1': win += 1
            wp[i] = win/total

            owp[i], num = 0, 0
            for j in range(N):
                if s[i][j]=='.': continue
                num += 1
                total, win = 0, 0
                for k in range(N):
                    if i==k: continue
                    if s[j][k]!='.': total += 1
                    if s[j][k]=='1': win += 1
                owp[i] += win/total
            owp[i] = owp[i]/num
        #print(wp,owp)
        
        for i in range(N):
            oowp[i], num = 0, 0
            for j in range(N):
                if s[i][j]!='.':
                    num += 1
                    oowp[i] += owp[j]
            oowp[i] = oowp[i]/num
            print(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i])

"""

if __name__ == '__main__':
    main()
