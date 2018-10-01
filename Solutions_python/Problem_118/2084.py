import math

input_file = 'C-small-attempt0.in'

d = {}

def isPalindrome(s):
	return s == s[::-1]

with open(input_file, 'r') as fin:
	with open('C-small-attempt0.out', 'w') as fout:
		T = int(fin.readline().rstrip())

		for i in range(0, T):
			A, B = map(int, fin.readline().rstrip().split(' '))

			count = 0
			for num in range(A, B+1):
				if d.get(num, False) or isPalindrome(str(num)):
					d[num] = True
					rt = math.sqrt(num)

					if (math.ceil(rt) == math.floor(rt)):
						rt = int(rt)

					if d.get(rt, False) or isPalindrome(str(rt)):
						d[rt] = True
						count += 1

			fout.write("Case #%s: %s\n" % (str(i+1), str(count)))