import sys
from sets import Set

sys.stdin = open('A-small-attempt0.in','r')
sys.stdout = open('A-small-attempt0.out','w')

def solve(case):
	a1 = int(raw_input())
	m1 = []
	m1.append(Set(map(int, sys.stdin.readline().strip().split())))
	m1.append(Set(map(int, sys.stdin.readline().strip().split())))
	m1.append(Set(map(int, sys.stdin.readline().strip().split())))
	m1.append(Set(map(int, sys.stdin.readline().strip().split())))

	a2 = int(raw_input())
	m2 = []
	m2.append(Set(map(int, sys.stdin.readline().strip().split())))
	m2.append(Set(map(int, sys.stdin.readline().strip().split())))
	m2.append(Set(map(int, sys.stdin.readline().strip().split())))
	m2.append(Set(map(int, sys.stdin.readline().strip().split())))

	intersect = m1[a1-1] & m2[a2-1]

	result = "None"
	if len(intersect) == 0:
		result = "Volunteer cheated!"
	elif len(intersect) > 1:
		result = "Bad magician!"
	else:
		result = str(intersect.pop())

	print "Case #" + str(case) + ": " + result


T = int(raw_input())
for t in xrange(T):
	solve(t+1)