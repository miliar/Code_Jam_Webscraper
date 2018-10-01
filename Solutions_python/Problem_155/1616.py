from __future__ import division
from cjlib.input import *
from cjlib.runner import TaskRunner, MPQRunner, DummyRunner
from itertools import permutations

get("""4
4 11111
1 09
5 110011
0 1""")

def process(data):
	out = 0
	current = 0
	for minPpl, count in enumerate(data[1]):
		count = int(count)
		if minPpl > current and count > 0:
			add = minPpl - current
			out += add
			current += add
		current += count
	return out

r = TaskRunner(process, DummyRunner)

while neof():
	r.add(line().split(" "))

r.run(True)