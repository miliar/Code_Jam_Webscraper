import sys
from math import sqrt, ceil

file = sys.argv[1]
text = open(file)
lines = text.readlines()

cases = lines.pop(0);

fair_squares = []



def is_palindrome(n):
	n = str(n)
	if len(n) == 1 or len(n)==0:
		return True
	if n[0] == n[-1]:
		return is_palindrome(n[1:-1])
	return False

for i in range(1, ceil(sqrt(10**14)//1)):
	a = i**2
	if is_palindrome(i) and is_palindrome(a):
		fair_squares.append(a)

def count_fair_square(start, end):
	total = 0
	start = int(start)
	end = int(end)
	for i in fair_squares:
		if i in range(start, end+1):
			total+=1
	return total

def main():
	i = 1
	while len(lines) > 0:
		line = lines.pop(0)
		bounds = line.split(' ')
		num_square_fair = count_fair_square(bounds[0], bounds[1])
		print("Case #{0}: {1}".format(i, num_square_fair))
		i+=1

main()