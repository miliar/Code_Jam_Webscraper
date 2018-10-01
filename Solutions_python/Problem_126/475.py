import sys
import math

DEBUG = True

def debug(input):
	if DEBUG:
		sys.stderr.write(input + '\n')

def main():
	t = int(sys.stdin.readline())
	for case in range(1, t+1):
		debug('processing case %d' % case)
		process_case(case)
	sys.stderr.write('Finished!\n')

def has_vowels(s):
	return any((c in set('aeiou')) for c in s)

def process_case(case):
	vals = sys.stdin.readline().split()
	s = str(vals[0])
	n = int(vals[1])
	l = len(s)
	val = 0
	num = 0
	hit = -1
	for start in range(l - n + 1):
		end = start + n
		sub = s[start:end]
		if not has_vowels(sub):
			debug(sub)
			debug('%d' % start)
			num += 1
			val += ((start - hit) * (l - end + 1))
			hit = start

	sys.stdout.write('Case #%d: %d\n' % (case, val))

if __name__ == '__main__':
	main()
