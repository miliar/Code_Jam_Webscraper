def scores (n):
    q=n/3
    r=n%3
    if r==0:
        return (q,q,q)          #3q
    elif r==1:
        return (q,q,q+1)        #3q+1
    else :
        return (q,q+1,q+1)      #3q+2

def sursco (n):
    q=n/3
    r=n%3
    if r==2:
        return (q,q,q+2)        #3q+2
    elif r==0:
        if q==0 or q==10:
            return (-1,-1,-1)
        else:
            return (q-1,q,q+1)      #3q
    else:
        if q==0:
            return (-1,-1,-1)
        else:
            return (q-1,q+1,q+1)      #3q+1

def best(total,p):
    n=scores(total)[2]
    s=sursco(total)[2]
    if n>=p :
        return 2
    elif s>=p :
        return 1
    else:
        return 0

def maxi(scores, surps, p):
    n=0
    s=0
    l=0
    scores = map(lambda x: best(x,p), scores)
    while (scores != []):
        tmp = scores[0]
        if tmp == 0:
            l += 1
        elif tmp == 1:
            s += 1
        elif tmp == 2:
            n += 1
        scores = scores[1:]
#    print n, s, l
    return (n+min(surps,s))

i = open('input', 'r')
n = int((i.readline())[:-1])
j=0
il=[]
while(j<n):
    il = il+[((i.readline())[:-1])]
    j += 1

import re
r=' '
il = map(lambda x: map(lambda y:int(y),re.split(r,x)),il)

def count (l):
    n = len(l)
    i=0
    ol = []
    while (i<n):
        t = "Case #"+str(i+1)+": "+str(maxi(l[i][3:],l[i][1],l[i][2]))
        ol = ol+[t]
        i += 1
    return ol

def show(l):
    if l==[]:
        return ""
    elif len(l)==1:
        return l[0]
    else:
        return l[0]+"\n"+show(l[1:])

print show(count(il))
