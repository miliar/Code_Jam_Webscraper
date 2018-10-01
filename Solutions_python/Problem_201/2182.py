def bathroom(room, people):
    if room == people: return (0,0)
    temp = [room]
    for x in temp:
        if x == 1: break
        temp.append((x-1)/2+(x-1)%2)
        temp.append((x-1)/2)
    temp = sorted(temp,reverse = True)
    if people-1 > len(temp): return (0,0)
    return ((temp[people-1]-1)/2 + (temp[people-1]-1)%2, (temp[people-1]-1)/2)

#print bathroom(999,499)

t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    print ("Case #%d: %d %d" %(i,bathroom(n,m)[0],bathroom(n,m)[1]))

