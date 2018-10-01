import sys
from copy import copy

def play_war(n, k):
	n.sort()
	n.reverse()
	k.sort()
	k.reverse()
	score = 0
	while len(n) > 0:
		if n[0] > k[0]:
			score += 1
			del(n[0])
			del(k[-1])
		else:
			del(n[0])
			del(k[0])
	return score

def play_deceitful_war(n, k):
	n.sort()
	n.reverse()
	k.sort()
	k.reverse()
	score = 0
	while len(n) > 0:
		if n[0] > k[0]:
			score += 1
			best_block = 0
			for i in range(len(n)):
				if n[i] > k[-1]: best_block = i
			del(n[best_block])
			del(k[-1])
		else:
			del(n[-1])
			del(k[0])
	return score

test_count = int(sys.stdin.readline())

for test_id in range(1, test_count + 1):
	N = int(sys.stdin.readline())
	blocks_naomi = list(map(float, sys.stdin.readline().split(' ')))
	blocks_ken  = list(map(float, sys.stdin.readline().split(' ')))
	war_score = play_war(copy(blocks_naomi), copy(blocks_ken))
	deceitful_war_score = play_deceitful_war(copy(blocks_naomi), copy(blocks_ken))
	print('Case #%d: %d %d' % (test_id, deceitful_war_score, war_score))
