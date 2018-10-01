import sys, os, string, re

line = sys.stdin.readline()
T = int(line)

for case_num in range(1, T+1):
	line = sys.stdin.readline()
	parts = line.split()
	N = int(parts[0])
	K = int(parts[1])

	sys.stdout.write('Case #%d: ' % case_num)
	if K%(2**N) == 2**N-1:
		sys.stdout.write('ON')
	else:
		sys.stdout.write('OFF')
	sys.stdout.write('\n')
