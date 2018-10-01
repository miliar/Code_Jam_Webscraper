#!/usr/bin/env python
from bisect import bisect_left

class War:
	def __init__(self, N, naomis, kens):
		self.N = N
		self.naomis = naomis[:]
		self.kens = kens[:]

	def chosenKen(self, told_naomi):
		chosen_index = 0
		if self.kens[-1] > told_naomi:
			chosen_index = bisect_left(self.kens, told_naomi)
		return self.kens.pop(chosen_index)

	def chosenAndToldNaomi(self):
		chosen = told = self.naomis.pop()
		return chosen, told

	def play(self):
		naomis_score = 0
		for i in range(N):
			chosen_naomi, told_naomi = self.chosenAndToldNaomi()
			chosen_ken = self.chosenKen(told_naomi)
			if chosen_naomi > chosen_ken:
				naomis_score += 1
		return naomis_score


class DeceitfulWar(War):
	def chosenAndToldNaomi(self):
		if len(self.naomis) > 1:
			for i in range(len(self.naomis)):
				if self.naomis[i] > self.kens[0]:
					chosen = self.naomis.pop(i)
					told = self.kens[-1] + 1
					return chosen, told
			chosen = self.naomis.pop(0)
			a = self.kens[-2]
			b = self.kens[-1]
			told = a + (b - a) / 2.0
		else:
			chosen = told = self.naomis.pop(0)
		return chosen, told

def getFloats():
	return sorted(map(float, raw_input().split()))

T = int(raw_input())
for t in range(T):
	N = int(raw_input())
	naomis = getFloats()
	kens = getFloats()
	deceitful_war = DeceitfulWar(N, naomis, kens)
	war = War(N, naomis, kens)
	print 'Case #{0}: {1} {2}'.format(
		t + 1,
		deceitful_war.play(),
		war.play())
