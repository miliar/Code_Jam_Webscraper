def dist(n1,l):
    k = []
    for w in range(len(l)):
        temp = (n1-l[w][0])*1.0/l[w][1]
        k.append(temp)
    return max(k)
    
f = [line.rstrip() for line in open('/Users/roshil/Desktop/A-small-attempt0.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for j in range(1, testcases+1):
    m = f[line].split()
    line += 1
    n1,n2 = m[0], int(m[1])
    kk = []
    for z in range(int(n2)):
        temp = [int(a) for a in f[line].split()]
        kk.append(temp)
        line  += 1
    #print kk
    ans = (int(n1)/dist(int(n1),kk ))
    #out.write("Case #"+str(j)+":"+ "\n")
    #print "Case #"+str(j)+":"+ "\n"
    #for lll in ans:
    #    out.write(''.join(lll) + "\n")
        #print ''.join(lll)
    out.write("Case #"+str(j)+": "+str(ans) + "\n")
    print "case #"+str(j)+": "+str(ans) + "\n"
out.close()