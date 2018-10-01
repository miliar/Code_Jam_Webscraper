a=int(input())
for i in range(a):
    b=int(input())
    while True:
        listn=[]
        listn.extend(str(b))
        if listn==sorted(listn):
            print('Case #'+str(i+1)+': '+str(b))
            break
        b-=1
