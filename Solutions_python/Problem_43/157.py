import sys

def main():
	nums = list("1023456789abcdefghijklmnopqrstuvwxyz")
	#nums_base = list("0123456789abcdefghijklmnopqrstuvwxyz")
	#f = file("test1.txt")
	f = file("A-large.in")
	f.readline();
	cnt = 0
	for l in f:
		idx = 0
		m = {}
		for c in l.strip():
			if not m.has_key(c):
				m[c] = nums[idx]
				idx += 1
		res = ""
		for c in l.strip():
			res += m[c]
		#print res, len(m)
		#print int(res, len(set(l.strip())))
		cnt += 1
		#print l.strip(), res,
		nbase = len(set(l.strip()))
		if nbase == 1: nbase = 2
		print "Case #%d: %d" % (cnt, int(res, nbase))

if __name__ == "__main__": main()
