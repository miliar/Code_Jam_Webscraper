import sys
sys.path.append("/Users/jevenson/pers/pers/googlecode")
import base

def is_tidy(target):
	nums = [int(s) for s in str(target)]
	if len(nums) < 2:
		return True
	i = 1
	while i < len(nums):
		if nums[i] < nums[i-1]:
			return False
		i += 1
	return True

def tidify(target):
	nums = [int(s) for s in str(target)]
	if len(nums) < 2:
		return
	i = len(nums) - 1
	while i > 0:
		if nums[i] < nums[i-1]:
			target -= int(''.join([str(n) for n in nums[i:]])) + 1
			nums = [int(s) for s in str(target)]
		i -= 1
	return target

def solve(problem):
  #@problem: (list of list of int) a list where each item is one of the
  #lines in the problem. Each item is also a list, of each number in
  #the line parsed and separated
  #
  #@return: (str) the solution to be printed

	target = problem[0]
	while target > 0:
		if is_tidy(target):
			return target
		target = tidify(target)
	return 0

if __name__ == "__main__":
    base.main(solve)
