def main():
    T=int(input())
    i=1
    while i<=T:
        n=input()
        l=len(n)
        t=int(n)
        if(l==1):
            print("case #",i,": ",t,sep='')
        else:
            for r in range(l-1,0,-1):
                if(int(n[r-1])>int(n[r])):
                    t=t-(int(n[r:l])+1)
                    n=str(t)
            print("case #",i,": ",t,sep='')
        i=i+1
main()
