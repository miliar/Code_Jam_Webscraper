def solve(a):
    charge=0
    f=0
    if len(a) == 1:return int(a)
    for n in range(len(a)-1):
        if int(a[n]) > int(a[n+1]):
            return int(a)-int(a[n+1-charge:])-1
        elif int(a[n]) == int(a[n+1]):
            charge+=1
    return int(a)

t=int(input())
for i in range(1,t+1):
    a=input()
    print('Case #{0}: {1}'.format(i,solve(a)))
        
