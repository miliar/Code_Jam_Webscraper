t = int(input())

def flip(s,f,l): #s is the string, f is "from", l is how long.
    r=s[:f]
    for i in range(f,f+l):
        if s[i]=='+':
            r+='-'
        else:
            r+='+'
    return r+s[f+l:] #define block is working


def flip_pancakes(s,l): #s is the string, l is how long
    d=[]
    for i in range(len(s)-l+1):
        d.append(flip(s,i,l))
    return d


for i in range(1, t + 1):
    s, l = input().split(' ')
    l=int(l) #length of the flipper
    c=1 #count of how many times flip the pancakes
    p=flip_pancakes(s,l)
    while not '+'*len(s) in p:
        if not '-' in s:
            c=0
            break
        c+=1
        t=[]
        ll=len(p)
        for j in p:
            t+=flip_pancakes(j,l)
        p+=t
        p=list(set(p))
        if len(p)==ll:
            c='IMPOSSIBLE'
            break
    print("Case #{}: {}".format(i, c))
