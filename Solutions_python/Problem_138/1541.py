#!/usr/bin/python

import sys

T = int(sys.stdin.readline().strip())

# Ken strategy: take lowest weight he has s.t.
# it is higher than what Naomi tells him
def war(N, naomi, ken):
	naomi.sort()
	ken.sort()
	cnt_ken = cnt_naomi = 0
	for n in range(N):
		naomi_choose = naomi.pop()
		if naomi_choose > max(ken): # Naomi is winning this one
			cnt_naomi += 1
			ken.pop(0) # Ken rids of his lowest weight
			continue
		for i in range(len(ken)): # Ken is winning this one
			if ken[i] > naomi_choose: # First one (lowest) to beat Naomi
				ken.pop(i)
				cnt_ken += 1
				break
	return cnt_naomi

# Deceitful war. Naomi first uses her highest weights, then decieves Ken.
def deceit(N, naomi, ken):
	naomi.sort()
	ken.sort()
	cnt_ken = cnt_naomi = 0
	for n in range(N):
		if max(naomi) > max(ken): # Use the max ones first
			naomi.pop()
			ken.pop()
			cnt_naomi += 1
			continue
		if min(naomi) > max(ken): # Naomi will win the rest
			cnt_naomi += N-n
			return cnt_naomi
		# if above if untrue, then there is a naomi < ken
		naomi.pop(0) # choose smallest but say it's just below Ken's max
		ken.pop() # to win Ken picks his max
		cnt_ken += 1
	return cnt_naomi

for i in range(1,T+1):
	N = int(sys.stdin.readline().strip())
	naomi = [float(x) for x in sys.stdin.readline().strip().split()]
	ken = [float(x) for x in sys.stdin.readline().strip().split()]
	print "Case #%s: %s %s" % (i, deceit(N, naomi[:], ken[:]), war(N, naomi[:], ken[:]))



