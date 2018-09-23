def istidy(n):
    l = [int(i) for i in str(n)]
    return all(l[i] <= l[i + 1] for i in xrange(len(l) - 1))

def last_tidy(n):
    for i in xrange(n,0,-1):
        if istidy(i):
            return i
            break

f=open('B-small-attempt0.in','r')
g=open('output_small.txt','w')
nt=int(f.readline().strip())
for i in range(nt):
    t=int(f.readline().strip())
    txt='Case #{0}: {1}'.format(i+1,last_tidy(t))
    g.write(txt)
    g.write('\n')
g.close()
f.close()
