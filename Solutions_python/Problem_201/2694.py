
f = open('C-small-1-attempt0.in','r')
w = open('C-attempt0.txt','w')
#Start
T = int(f.readline())


    
for j in range(0, T):
    NK = (f.readline()).split(' ')#f.readline()
    N = int(NK[0])
    K = int(NK[1])
    currLS = 0
    currRS = 0
    B = [N] #Single subset of length N
    for i in range(0, K):
        buff = []
        b = max(B)
        if b % 2 == 1:
            buff.append((b-1)/2)
            buff.append((b-1)/2)
        if b % 2 == 0:
            buff.append(b/2-1)
            buff.append(b/2)
        B.remove(b)
        t= 0
        for bu in buff:
            if bu != 0:
                B.insert(t,bu)
                t += 1
        if i == K-1:
            if j == T-1:
                w.write("Case #%i: %s %s" %(j+1, max(buff), min(buff)))
            else:
                w.write("Case #%i: %s %s\n" %(j+1, max(buff), min(buff)))


#End
w.close()
print "Done"
