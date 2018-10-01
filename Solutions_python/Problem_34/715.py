# coding: cp932
import itertools
import time

def main():
	fi = open('large_a.txt')
	##fo = open('a_out.txt', 'w')
	L, D, N = [int(tok) for tok in fi.readline().strip().split()]
	words = []
	for i in range(D):
		words.append(fi.readline().strip())
	ptns = []
	for i in range(N):
		ptns.append(fi.readline().strip())
	# check for each case
	for i in range(N):
		ptn = ptns[i]
		ptn_ = split_ptn(ptn)
		cnt = 0
		is_ok = True
		for word in words:
			is_ok = True
			for w, pt in zip(word, ptn_):
				#print w, pt
				if w not in pt:
					is_ok = False
					break
			if is_ok:
				cnt += 1
		print('Case #%d: %d' % (i+1, cnt))
	fi.close()
	##fo.close()

def split_ptn(ptn_s):
	L = []
	while True:
		if not ptn_s:
			return L
		if ptn_s.find('(') != 0:
			L.append(ptn_s[0])
			ptn_s = ptn_s[1:]
			continue
		else:
			st = ptn_s.find('(')
			ed = ptn_s.find(')')
			L.append(ptn_s[st+1:ed])
			ptn_s = ptn_s[ed+1:]
	return L

if __name__ == '__main__':
	import psyco
	psyco.full()
	main()
	#print split_ptn('k(kmnx)qe(xykn)jwevx')
	