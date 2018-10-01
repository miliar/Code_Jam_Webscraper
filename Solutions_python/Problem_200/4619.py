import sys

def isSorted(n):
	if n > 9:
		prev_dig = n % 10
		n = n / 10
		while n > 0:
			cur_digit = n % 10
			if cur_digit > prev_dig:
				return False
			prev_dig = cur_digit
			n = n / 10
		return True
	return True
		
def solve(n):
	while (n >= 10):
		if isSorted(n):
			return n
		n = n - 1
	return n

def solution(fname):
	with open(fname) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	cases = int(content[0])
	nums = []
	for case in range(cases):
		n = int(content[case+1])
		nums.append(solve(n))

	for n in range(len(nums)):
		print "Case #" + str(n+1) + ": " + str(nums[n])


def main():
	sys.stdout = open("tidy_output.txt", "w")
	solution("test.txt")

main()

