#!/usr/local/bin/python3

def chk(a):
    return str(a) == ''.join(sorted(str(a)))

def update(a):
    x = 0
    for i in range(1,len(a)):
        if int(a[i]) < int(a[i-1]):
            x = i
            break
    n = str(int(a[:x])-1) + '9'*(len(a)-x)
    return n

t = int(input())
for cs in range(1,t+1):
    n = input()
    while(not chk(n)):
        n = update(n)
    print("Case #%d: %d"%(cs,int(n))) 
