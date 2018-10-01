def main():
    T=(int)(input())
    for aaa in range(T):
        a=raw_input().split(' ')
        r=(int)(a[0])
        t=(int)(a[1])
        strin='Case #'+str(aaa+1)+': '
        s=0
        tr=r
        count=0
        p=0
        while s<=t:
            p=2*tr+1
            #print p
            if(s+p>t):
                break
            s=s+p
            count+=1
            tr+=2
        print strin+str(count)
if __name__=='__main__':
    main()
            
