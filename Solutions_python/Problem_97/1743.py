def rotation(lala,n1,n2):
    results = []
    z = lala[1:] + lala[0]
    if (n1 <= int(z) <= n2) and (int(z)>int(lala)): # need to get the first z!
            results.append((lala,z))
    while z != lala:
        z = z[1:] + z[0]
        if (n1 <= int(z) <= n2) and (int(z)>int(lala)): # second part is to avoid duplicates
            results.append((lala,z))
    return results
  
hand = open('C-large.in')
count = 0
for line in hand:
    m = line.split()
    if len(m) > 1:
        count += 1
        res = []
        n = int(m[0])
        while n < int(m[1]):
            f = rotation(str(n),int(m[0]),int(m[1]))
            res.extend(f)
            n += 1
        print "Case #%d: %d" %(count,len(res))
