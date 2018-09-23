import JamFiles as Files, math, queue

def parseLine(line):
    first = line.split(" ")
    if len(first) > 1:
        second = (int(first[0]),int(first[1]))
        return second
    else:
        return first

def maxKey(a):
    return (a[0],-a[1])

def update(dist):
    #s = max(dist, key=maxKey)
    #dist = [x for x in dist if x != s]
    s = dist.get()
    d,l,r = -s[0],s[1],s[2]
    newS = l + math.ceil(d/2) - 1
    L1,R1 = l, newS-1
    L = (R1-L1+1,L1,R1)
    L2 = newS+1
    R2 = r
    R = (R2-L2+1,L2,R2)
    if (L[0] > 0):
        dist.put((-L[0],L[1],L[2]))
    if (R[0] > 0):
        dist.put((-R[0],R[1],R[2]))
    return dist
    
def yz(dist):
    #dist2 = update(dist)
    #lr = [x for x in dist2 if x not in dist]
    #lr = dist2[:]
    lr = -dist.get()[0]
    #lr = 
    #lr = max(dist)[0]
    lr -= 1
    y = math.ceil(lr/2)
    z = math.floor(lr/2)
    #print (lr)
    #y = max(lr)[0]
    #z = min(lr)[0]
    return ("%s %s" % (y,z))

def iterate(N):
    dist = queue.PriorityQueue()
    dist.put((-N[0],0,N[0]-1))
    k = N[1]
    for i in range(k-1):
        dist = update(dist)
    return yz(dist)
#dist = [(1000,0,999)]
#dist = update(dist)
#print (yz(dist))


ans = []
i = 0
start = int(input("Start at? "))
contents = Files.readToContents(parseLine, "l2.in")[1:]
for b in range(0,start):
    ans.append("n")
for N in range(start,start+20):#contents:
    if N < len(contents):
        ans.append(iterate(contents[N]))
    i += 1
    print ("Progress: " , i)

Files.writeFile(ans, Files.syntax, "OutLoos%s.txt" % start)

print ("Done!")
