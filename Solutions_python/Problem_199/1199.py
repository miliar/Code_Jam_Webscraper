t = int(input())
np = "IMPOSSIBLE"
for r in range(t):
        [s,k] = input().split()
        print ("Case #",r+1,':',sep='',end = ' ')
        k = int(k)
        s = list(s)
        l = len(s)
        count = 0
        imp   = True   
        for i in range(l-k+1):
                if s[i] == '-':
                        for j in range(i,i+k):
                                if s[j] == '+':
                                        s[j] = '-'
                                else:
                                        s[j] = '+'       
                        count += 1
                
        for  i in range (l-k,l):
                if s[i] == '-':
                        print (np)
                        imp = False
                        break;   
        if imp:
                print(count)                                                    
                     
