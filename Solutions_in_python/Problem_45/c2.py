from __future__ import with_statement
#import psyco
#psyco.full()

def process_case(data, out):

    def release(q, p):
	p[q] = 0
	qr = q+1
	ql = q-1
	c = 0
	ans = 0
	while qr < len(p) and p[qr]:
	    ans += 1
	    qr += 1
	    if qr == len(p):
		break
	while (ql >= 0) and p[ql]:
	    ans += 1
	    ql -= 1
	    if ql < 0:
		break
	return ans

    def release_all(qs, p):
	ans = 0
	if len(qs) < prisonerct:
	    return 999999999999999
	#print "releasing all", qs
	for q in qs:
	    #print q, ans
	    ans += release(q, p)
	return ans
    
    def order(qs, start, end, o = None):
#	import pdb; pdb.set_trace()
	if o == None: o = []
	p = (end - start + 1)
	mid = (end - start + 1) / 2 + start
	px = (end - start) % 2
	i = 0
	while qs and i < p:
	    if (mid + i) in qs:
		if ((mid - px - i) in qs) and i:
		    no = o[:]
		    no.append(mid - px - i)
		    nql = [q for q in qs if q < (mid - px - i)]
		    nqr = [q for q in qs if q > (mid - px - i)]
		    for litem in order(nql, start, mid - px - i - 1):
			for ritem in order(nqr, mid - px - i + 1, end):
			    yield no + litem + ritem
		o.append(mid + i)
		qs.remove(mid + i)
		nql = [q for q in qs if q < (mid + i)]
		nqr = [q for q in qs if q > (mid + i)]
		for litem in order(nql, start, mid + i - 1,):
		    for ritem in order(nqr, mid + i + 1, end):
			yield o + litem + ritem
	    elif (mid - px - i) in qs:
		o.append(mid - px - i)
		qs.remove(mid - px - i)
		nql = [q for q in qs if q < (mid - px - i)]
		nqr = [q for q in qs if q > (mid - px - i)]
		for litem in order(nql, start, mid - px - i - 1):
		    for ritem in order(nqr, mid - px - i + 1, end):
			yield o + litem + ritem
	    i += 1
	if not qs:
	    #print qs, "yielding", order
	    yield o
	else:
	    o.extend(qs[:])
	    yield o
		
    def permute(l):
	if len(l) == 1:
	    yield l
	else:
	    for i,x in enumerate(l):
		for p in permute(l[:i] + l[i+1:]):
		    yield [x] + p   
    p, prisonerct = map(int, data.readline().strip("\n").split(" "))
    qs = [x-1 for x in map(int, data.readline().strip("\n").split(" "))]
    ps = [1] * p
	
    #ans = min( release_all(o, ps[:]) for o in order(qs[:], 0, p - 1))
    ans = min(release_all(o, ps[:]) for o in permute(qs))
    print ans
    out.write("%d\n" % (ans))
    return
    #out.write("%s\n" % new)
    #out.write('\n'.join((' '.join(x for x in row) for row in basin)))

def process_file(fname):    
    
    with open(fname, "r") as data:
	with open("answer_" + fname, "w") as answer:
	    n = int(data.readline().strip("\n"))
	    for i in range(n):
		answer.write("Case #%d: " % (i+1))
		process_case(data, answer)
process_file("csample.txt")
process_file("C-small-attempt4.in")
#process_file("C-large.in")