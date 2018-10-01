# Author: Brian Armstrong
# Code Jam 2009
# Qualification Round
# Problem C: Welcome to Code Jam

import sys, os
import string

phrase = 'welcome to code jam'


class CharMap(object):
	def __init__(self, phrase):
		self.dict = {}
		self.phrase = list(phrase)
		for char in self.phrase:
			# will overwrite itself a bit here, but that's ok
			self.dict[char] = []
		self.memo = {}
	def _scan(self, case):
		k = self.dict.keys()
		n = 0
		for n in range(0, len(case)):
			char = case[n]
			if char in k:
				self.dict[char].append(n)

		for key in self.dict:
			self.dict[key].sort()

	def _find(self, index, remain):
		if (index, len(remain)) in self.memo:
			return self.memo[(index, len(remain))]

		if len(remain) == 0:
			return 1
		last = remain.pop()
		n = 0
		for i in self.dict[last]:
			if index < i:
				break #sorted, only gets bigger from here
			n += self._find(i, remain)

		remain.append(last)
		self.memo[(index, len(remain))] = n
		return n


	def findphrase(self, case):
		self._scan(case)
		remain = self.phrase[:]
		last = remain.pop()

		n = 0
		for i in self.dict[last]:
			n += self._find(i, remain)

		return n


def print_cases(cases):
	n = 1
	for case in cases:
		print "Case #" + str(n) + ": " + str(case).zfill(4)[-4:]
		n = n + 1

def main():
	input_n = int(sys.stdin.readline().rstrip())
	cases = []
	for n in range(0, input_n):
		case = sys.stdin.readline().rstrip()

		cm = CharMap(phrase)

		cases.append(cm.findphrase(case))

	print_cases(cases)


if __name__ == "__main__":
	main()


