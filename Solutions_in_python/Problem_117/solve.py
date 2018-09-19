
def begin(w,h):
	return [
		[100 for _ in xrange(w)] for _ in xrange(h)
	]
def read_lawn(w,h):
	lawn = begin(w,h)
	for i in range(h):
		s = raw_input().split()
		for j,n in enumerate(s):
			lawn[i][j] = int(n)
	return lawn

def heights(lawn):
	n = []
	for row in lawn:
		n.extend(row)
	n = list(set(n))
	n.sort(reverse=True)
	return n



def valid(lawn):
	width = len(lawn[0])
	height = len(lawn)
	def valid_pixel(i,j,h):
		col = [lawn[y][j] for y in range(height)]
		row = lawn[i]
		return max(col)<=h or max(row)<=h

	for i,row in enumerate(lawn):
		for j,h in enumerate(row):
			if not valid_pixel(i,j,h):
				return False
	return True

tcases = int(raw_input())
for d in xrange(tcases):
	h,w = tuple(map(int,raw_input().split()))
	lawn = read_lawn(w,h)
	if valid(lawn):
		print "Case #%d: YES" % (d+1)
	else:
		print "Case #%d: NO" % (d+1)

