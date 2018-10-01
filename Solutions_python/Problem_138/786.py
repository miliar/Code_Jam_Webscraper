#! /usr/bin/python

import sys

def war(naomi, ken):
	pts = 0
	naomi.reverse()
	for idx, blk in enumerate(naomi):
		kc = 0
		for idy, kblk in enumerate(ken):
			if kblk > blk:
				kc = ken[idy]
				break
		if (kc == 0):
			kc = ken[0]
		ken.remove(kc)
		if blk > kc:
			pts += 1
	return pts



def dwar(naomi, ken):
	pts = 0
	rnds = len(naomi)
	for rnd in range(rnds):
		if naomi[-1:][0] < ken[-1:][0]:
			naomi.remove(naomi[0])
			ken.remove(ken[-1:][0])
		elif naomi[-1:][0] > ken[-1:][0]:
			pts += 1
			naomi.remove(naomi[-1:][0])
			ken.remove(ken[-1:][0])
		elif naomi[-1:][0] > ken[0]:
			pts += 1
			naomi.remove(naomi[-1:][0])
			ken.remove(ken[0])
		else:
			naomi.remove(naomi[0])
			ken.remove(ken[-1:][0])
	return pts

trials = int(sys.stdin.readline())

for rnd in range(trials):
	blk_cnt = int(sys.stdin.readline())
	n_blks = [ float(x) for x in sys.stdin.readline().split(" ") ]
	k_blks = [ float(x) for x in sys.stdin.readline().split(" ") ]
	n_blks.sort()
	k_blks.sort()

	n_war = list(n_blks)
	n_dwar = list(n_blks)
	k_war = list(k_blks)
	k_dwar = list(k_blks)
	war_pts = war(n_war, k_war)
	dwar_pts = dwar(n_dwar, k_dwar)

	print 'Case #%d: %d %d' % (rnd + 1, dwar_pts, war_pts)
