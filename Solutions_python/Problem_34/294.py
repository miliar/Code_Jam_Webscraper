import sys
import psyco
psyco.full()

def main():
	l, d, n = [int(i) for i in sys.stdin.readline().split()]
	x, lang = 0, []
	for i in range(d):
		lang.append(sys.stdin.readline().strip())
	for i in range(n):
		toks, k, p = sys.stdin.readline().strip().split(')'), 0, []
		for t in toks:
			if t and t[0] == '(':
				p.append(t[1:])
			else:
				p.extend(t)
		for l in lang:
			k += 1
			for i in range(len(l)):
				if l[i] not in p[i]:
					k -= 1
					break
		x += 1
		print 'Case #%d: %d' % (x, k)

main()
