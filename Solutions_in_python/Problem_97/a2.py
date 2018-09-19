from collections import deque

fin = open('a2-test.txt')
fo = open("a2-out.txt","w")
fin.readline()

for case, l in enumerate(fin):
    t = l[:-1].split()
    a = int(t[0])
    b = int(t[1])

    print (case + 1),a,b,

    d = {}
    #f = [0] * (b + 1)
    for i in xrange(1, b + 1):
	ss = str(i).zfill(len(t[0]))
	#if f[i] == 1:
	#    continue
	dq = deque(ss)
	#print dq 
	for j in xrange(0, len(dq)):
	    dq.rotate(1)
	    s = "".join(dq)
	    x = int("".join(dq))
	    if a <= i and i < x and x <= b:
		d[(i,x)] = 1
		#f[x] = 1
    fo.write("Case #{}: {}\n".format(case + 1, len(d)))
    print len(d)
