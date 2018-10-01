# /usr/bin/python
import sys
import math

def dbg(s): sys.stderr.write(str(s) +"\n")
def reads(t): return map(t, input().split(" "))
def read(t) : return t(input())


palss = {
	0: [],
	1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	2: [11, 22, 33, 44, 55, 66, 77, 88, 99],
}
pals = palss[1] + palss[2]
fsq = []



def gen_pals(n):
	
	ps = palss.get(n)
	if ps != None:
		return ps
	
	p_list = gen_pals(n-2)
	ps = []
	for i in range(1, 10):
		for p in p_list:
			np = int(str(i) + str(p) + str(i))
			ps.append(np)
			pals.append(np)

	palss[n] = ps	
	return ps

def gen_fsq(max_fsq):
	for p in pals:
		maybe_fsq = p**2
		if maybe_fsq > max_fsq:
			return
		if maybe_fsq in pals_set:
			fsq.append(maybe_fsq)


G = 3
for i in range(1, G+1):
	gen_pals(i)

pals.remove(0)
max_pal = pals[-1]
pals_set = set(pals)

gen_fsq(max_pal)

T = read(int)

for t in range(1, T+1):
	[A, B] = reads(int)
	
	cnt = 0
	for f in fsq:
		if f >= A and f <= B:
			cnt += 1

	print("Case #%d: %d" % (t, cnt))
