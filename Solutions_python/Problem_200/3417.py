# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(raw_input())  # read a line with a single integer
p=[]
for b in xrange(1, t + 1):
    n=raw_input()
    c=1
    m=list(n)
    while c<len(m):
        if int(m[c])<int(m[c-1]):
            m[c-1]=int(m[c-1])-1
            for i in range(c,len(m)):
                m[i]=9
            c=1
        if int(m[c])>=int(m[c-1]):
            c+=1

    if c==len(m):
        if m[0]==0:
            m=m[1:]
        k=''.join(str(e) for e in m)
        p.append('Case #'+str(b)+': '+str(k))
for d in p:
    print d

    # check out .format's specification for more formatting options
