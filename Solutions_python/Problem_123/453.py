from sys import argv, stdin, stdout
from collections import defaultdict, deque
from operator import eq

fin = open(argv[1]) if len(argv) > 1 else stdin
fout = open(argv[2], 'w') if len(argv) > 2 else stdout


def bfs(start, end, edges, eq=eq):
	# edges is a function that returns an iterable
	# eq tests for equality between final state and cur state
	seen = set()
	q = deque()
	q.append(start)
	bt = {}
	bt[start] = None
	while q:
		cur = q.popleft()
		if cur in seen: continue
		seen.add(cur)
		if eq(cur, end):
			real_end = cur
			break
		for next in edges(cur):
			bt[next] = cur
			q.append(next)
	path = []
	last = real_end
	while last in bt and last is not None:
		path.append(last)
		last = bt[last]
	path.reverse()
	return path

def edges((a, m)):
	# go from an impossible state to a state
	# where one option was used
	#print a, m
	assert len(m) != 0 and a <= m[0]
	# add new thing
	new_a = 2 * a - 1
	if new_a > a:
		new_m = list(m)
		new_m.reverse()
		while new_m and new_a > new_m[-1]:
			new_a += new_m.pop()
		new_m.reverse()
		yield (new_a, tuple(new_m))
	# remove big thing
	yield (a, m[:-1])
	# remove big thing
	#new_a = a
	#new_m = list(m)
	#new_m.reverse()
	#new_m.pop()
	#while new_m and new_a > new_m[-1]:
	#	new_a += new_m.pop()
	#new_m.reverse()
	#yield (new_a, tuple(new_m))

def a_eq((a, m), (a2, m2)):
	return m == m2

def solve(a, m):
	# I did not realize at firt that the
	# order that the motes were taken up did not matter
	m = sorted(m)
	# get to start state
	m.reverse()
	while m and a > m[-1]:
		a += m.pop()
	m.reverse()
	path = bfs((a, tuple(m)), (None, ()), edges, a_eq)
	return len(path) - 1


N = int(fin.readline())
for case in xrange(1, N + 1):
	a, _ = map(int, fin.readline().split()) #armin
	m = map(int, fin.readline().split()) # other motes
	t = solve(a, m)
	fout.write('Case #%d: %d\n' % (case, t))
