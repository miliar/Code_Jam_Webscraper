from __future__ import print_function
import sys
import math

def main():
	t = int(sys.stdin.readline())
	for case in range(1, t+1):
		sys.stderr.write('processing case %d\n' % case)
		process_case(case)
	sys.stderr.write('Finished!\n')

def process_case(case):
	n = int(sys.stdin.readline())
	m = map(int, sys.stdin.readline().split())
	a_eaten = strategy_a(m)
	b_eaten = strategy_b(m)
	sys.stdout.write('Case #%d: %d %d\n' % (case, a_eaten, b_eaten))

def strategy_a(m):
	prev = m[0]
	eaten = 0
	for m_i in m[1:]:
		if m_i < prev:
			eaten += (prev - m_i)
		prev = m_i
	return eaten

def strategy_b(m):
	max_edible = get_max_lost(m)
	eaten = 0
	for m_i in m[:-1]:
		eaten += min(m_i, max_edible)
	return eaten

def get_max_lost(m):
	prev = m[0]
	max_lost = 0
	for m_i in m[1:]:
		diff = prev - m_i
		max_lost = max(max_lost, diff)
		prev = m_i
	return max_lost

def get_diffs(m):
	prev = m[0]
	diffs = []
	for m_i in m[1:]:
		diffs.append(prev - m_i)
		prev = m_i
	return diffs

if __name__ == '__main__':
	main()
