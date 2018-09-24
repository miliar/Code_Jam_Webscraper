# coding: cp932

def main():
	fi = open('in_large.txt')
	fo = open('out_large.txt', 'w')
	ncase = int(fi.readline())
	for i in range(ncase):
		ns = int(fi.readline())
		Ss = []
		for j in range(ns):
			Ss.append(fi.readline().strip())
		nq = int(fi.readline())
		Qs = []
		for j in range(nq):
			Qs.append(fi.readline().strip())
		# calc
		nsw = calc_switch(0, Ss, Qs)
		fo.write('Case #%d: %d\n' % (i+1, nsw))
	fi.close()
	fo.close()

def calc_switch(nsw, Ss, Qs):
	#print nsw, Ss, Qs
	if set(Ss) - set(Qs):
		return nsw
	S_d = dict([(S, True) for S in Ss])
	max_i = 0
	Q_d = {}
	for i, Q in enumerate(Qs):
		if Q not in Q_d:
			Q_d[Q] = i
			if max_i < i:
				max_i = i
	Qs = Qs[max_i:]
	return calc_switch(nsw+1, Ss, Qs)
	
import sys
sys.setrecursionlimit(100000)
main()
