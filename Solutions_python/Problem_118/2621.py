import sys, math

def isqrt(n):
	return (n ** 0.5) ** 2 == n

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]
def main():
	case = sys.argv[1]

	with open("C-%s.in" % case, 'rb') as fin:
		with open("C-%s.out" % case, 'wb') as fout:
			n_cases = int(fin.readline().strip())
			for c in xrange(1, n_cases+1):

				a, b = map(int, fin.readline().strip().split(" "))
				r = 0

				i = int(math.ceil(a ** 0.5))

				while i * i <= b:
					if is_palindrome(i) and is_palindrome(i * i): 
						r += 1
						print i, i*i
					i += 1

				print c, a, b, i, r

				fout.write("Case #%s: %s\n" % (c, r))

if __name__ == "__main__":
	main()