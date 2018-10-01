import sys

args = sys.argv[1:]

inputfile = args[0]
outputfile = inputfile+'.out'

f = open(inputfile)

l1 = f.readline().strip()
print l1
T = int(l1)

DIRS = [ (-1, 0), (0, -1), (0, 1), (1, 0) ]
REVDIR = [ 3, 2, 1, 0 ]
fo = open(outputfile, 'w')
case_no = 0
for t in range(T):
	lt = f.readline().rstrip('\r\n')
	case_no += 1
	lts = lt.split(' ')
	H = int(lts[0])
	W = int(lts[1])
	m = []
	for h in range(H):
		lth = f.readline().rstrip('\r\n')
		hi = [ int(hii) for hii in lth.split(' ') ]
		m.append(hi)
	#print m
	# mark the map with flow dir
	mm = []
	for h in range(H):
		mm.append([None]*W)
	#mm[0][0] = 1
	for h in range(H):
		for w in range(W):
			lowestv = m[h][w]
			lowesti = -1
			for di,dv in enumerate(DIRS):
				nh = h+dv[0]
				nw = w+dv[1]
				if nh>=0 and nh<H and nw>=0 and nw<W:
					if m[nh][nw]< lowestv:
						lowesti = di
						lowestv = m[nh][nw]
			#if lowesti != -1:
			mm[h][w]=lowesti
	#print mm
	# now do the labelling
	ml = []
	mi = []
	ms = []
	for h in range(H):
		ml.append([None]*W)
		mi.append([None]*W)
		ms.append([None]*W)
	for h in range(H):
		for w in range(W):
			ms[h][w] = [] # dir id that share same cluster as this cell
			if mm[h][w] == -1:
				for di,dv in enumerate(DIRS):
					nh = h+dv[0]
					nw = w+dv[1]
					if nh>=0 and nh<H and nw>=0 and nw<W:
						if mm[nh][nw] == REVDIR[di]: # flow into this cell
							ms[h][w].append(di)
			else:
				# should flow into another cell, share same cluster as that cell
				ms[h][w].append(mm[h][w])
	#print ms
	maxid = 1
	mi[0][0] = maxid
	idmap = {mi[0][0]: set([ mi[0][0] ])} # id -> set of id
	# first pass assign basin id first
	for h in range(H):
		for w in range(W):
			#if mm[h][w] is None:# skip those marked
			if len(ms[h][w])==0:
				maxid += 1
				mi[h][w] = maxid
				idmap[maxid] = set([])
			else:
				for di in ms[h][w]:
					nh = h+DIRS[di][0]
					nw = w+DIRS[di][1]
					if mi[nh][nw] is not None:
						if mi[h][w] is not None and mi[h][w] != mi[nh][nw]:
							# same basin, need to map id
							newset = idmap[mi[h][w]] | idmap[mi[nh][nw]]
							for idi in newset:
								idmap[idi]=newset # set to two sets to be teh same instance
						else:
							mi[h][w] = mi[nh][nw]
					else:
						if mi[h][w] is not None:
							mi[nh][nw] = mi[h][w]
						else:
							# both are None
							maxid += 1
							mi[h][w] = maxid
							mi[nh][nw] = maxid
							idmap[maxid] = set([maxid])
	#print mi
	#print idmap
	maxl = 97 # 97 is 'a'
	idlabelmap = { mi[0][0] : chr(maxl) } # id -> label
	for idi in idmap[mi[0][0]]:
		idlabelmap[idi] = chr(maxl)
	fo.write('Case #%d:\n' % case_no)
	for h in range(H):
		for w in range(W):
			cid = mi[h][w]
			label = idlabelmap.get(mi[h][w], None)
			if label is None:
				# assign new label
				maxl += 1
				label = chr(maxl)
				idlabelmap[cid] = label
				for idi in idmap[cid]:
					idlabelmap[idi] = label
			if w>0:
				fo.write(' ')
			fo.write(label)
		fo.write('\n')
f.close()
fo.close()

print "Done. written to %s" % outputfile
