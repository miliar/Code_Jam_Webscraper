FI = 'B-large.in'
#FI = 'in'

def case(fi, fo, n):
	nextlabel=1
	labels = {}
	H,W = zw([int,int],fi.readline().split())
	map = [None] * H
	for x in xrange(H):
		map[x] = [int(i) for i in fi.readline().split()]
	shadow = [[0] * W for i in xrange(H)]

	fo.write('Case #%d:\n' % (n))

	for j in xrange(H):
		for i in xrange(W):
			flow=[(i,j)]
			pi,pj = i,j
			while True:
				ca = map[pj][pi] 
				cd = (0,0)
				if pj > 0: #n
					if map[pj-1][pi] < ca:
						ca = map[pj-1][pi]
						cd = (0,-1)
				if pi > 0: #w
					if map[pj][pi-1] < ca:
						ca = map[pj][pi-1]
						cd = (-1,0)
				if pi < W-1: #e
					if map[pj][pi+1] < ca:
						ca = map[pj][pi+1]
						cd = (1,0)
				if pj < H-1: #s
					if map[pj+1][pi] < ca:
						ca = map[pj+1][pi]
						cd = (0,1)
				x, y = cd
				pi, pj = pi+x, pj+y
				flow += [(pi,pj)]
				if cd == (0,0) or shadow[pj][pi] != 0:
					break
			fi, fj = flow[-1]
			if shadow[fj][fi] == 0:
				shadow[fj][fi] = nextlabel
				nextlabel += 1
			for (pi, pj) in flow:
				shadow[pj][pi] = shadow[fj][fi]
	nextlabel = ord('a')
	for j in xrange(H):
		for i in xrange(W):
			lbl = shadow[j][i]
			if lbl not in labels:
				labels[lbl] = chr(nextlabel)
				nextlabel += 1
			fo.write('%s ' % (labels[lbl]))
		fo.write('\n')
			

# ---

def rl(f, n):
	return [f.readline() for i in xrange(n)]
def zw(fs, es):
	return [f(e) for f,e in zip(fs, es)]
def cases(fi, fo):
	for i in xrange(int(fi.readline())):
		case(fi, fo, i+1)

fi = open(FI)
fo = open('out.txt', 'w')
cases(fi, fo)
fi.close()
fo.close()

f = open('out.txt')
print f.read()
