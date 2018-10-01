def distanz(liste,pos,count):
    dc = -1
    while liste[pos] != 1:
        pos += count
        dc += 1
    return dc
def is_power2(num):
	return num != 0 and ((num & (num - 1)) == 0)
def next(liste):
    values = []
    for i in range(1,len(liste)):
        if not liste[i] or True:
            values.append((distanz(liste,i,-1),distanz(liste,i,1),i))
    mf = sorted([min(x[0],x[1]) for x in values])[-1]

    fl = list(filter(lambda x:min(x[0],x[1]) == mf,values))

    mhl = sorted(fl,key=lambda x:max(x[0],x[1]))[-1]
    mh = max(mhl[0],mhl[1])
    fl = list(filter(lambda x: max(x[0],x[1]) == mh, fl))
    #print(str(">> ")+str(mh)+" "+str(mf)+" "+str(fl[0][2]))
    return fl[0][2],mh,mf
def countit(n,k):
    liste = [1]+[0]*n+[1]
    for i in range(k):
        #print(i)
        x,m,h = next(liste)
        #print(x)
        liste[(x)] = 1
    return m,h
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    tc, m = [int(x) for x in (input().split(" "))]  # read a list of integers, 2 in this case
    y = countit(tc,m)
    print("Case #{}: {} {}".format(i, y[0],y[1]))
