def solve():
    t=int(input())
    for k in range(1,t+1):
        s=input()
        if int(s)<10 or all(s[i]<=s[i+1] for i in range(len(s)-1)):
            print("Case #{}: {}".format(k,s))
        else:
            exitflag=False
            for i in range(len(s)-1):
                if s[i]>=s[i+1]:
                    if s[i]=='1':
                        pow=0
                        temp=int(s)
                        while temp>=10:
                            temp/=10
                            pow+=1
                        exitflag=True
                        print("Case #{}: {}".format(k,10**pow-1))
                        break
                    else:
                        exitflag=True
                        pre=s[:i]
                        end=chr(ord(s[i])-1)+'9'*(len(s)-i-1)
                        print("Case #{}: {}".format(k,pre+end))
                        break
            if not exitflag:
                print("Case #{}: {}".format(k,s))

            

solve()
                        
                        
                    
