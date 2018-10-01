from math import sqrt

def is_palindrome(n):
	s = str(n)
	return True if s == s[::-1] else False

def is_fairly_square(n):
	sqrt_of_n = sqrt(n)
	return sqrt_of_n.is_integer() and is_palindrome(int(sqrt_of_n))

def is_fair_and_square(n):
	return True if is_palindrome(n) and is_fairly_square(n) else False

def main():
	f = open('1.in', 'r')
	o = open('1.out', 'w')

	T = int(f.readline().strip())

	for t in xrange(T):
		res = 0
		start, end = f.readline().split()
		#print start + ' ' + end
		for n in xrange(int(start), int(end) + 1):
			if is_fair_and_square(n):
				res += 1

		s = "Case #%d: %s\n" % (t+1, res)
		#print s
		o.write(s)

if __name__ == "__main__":
    main()
