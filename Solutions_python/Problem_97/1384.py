
def main(line):
        A = int(line[0])
        B = int(line[1])
        y = 0
        for n in xrange(A, B):
            if n < 10: continue
            s = str(n)
            l = len(s)
            h = set()
            for i in xrange(1, l):
                if s[l-i] == '0': continue
                m = int(s[l-i : l] + s[0 : l-i])
                if m <= B and n < m and m not in h:
                    y+=1
                    h.add(m)
        return y

if __name__ == '__main__':
	import sys
	N = int(sys.stdin.readline())
	for i in xrange(N):
		res = main(sys.stdin.readline().strip().split(' '))
		print "Case #%d: %i" % (i + 1, res)	
