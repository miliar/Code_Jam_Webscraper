a = []
for i in range(0,int(input())):
    a.append(int(input()))
def abd(x,j):
    while(1):
        if x%10 == x:
            print("Case #%d: %d" %(j,x))
            return
        else:
            b = sorted(list(str(x)))
            c = ''.join(str(z) for z in b)
            if str(x) == c:
                print("Case #%d: %d" %(j,x))
                return
            else:
                x -= 1
for i in range(0,len(a)):
    abd(a[i],i+1)         
