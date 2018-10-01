import sys

def solve(s):
	people_up,people_needed = 0,0
	for i in range(len(s)):
		if(people_up < i):
			people_needed += i-people_up
			people_up = i
		people_up += s[i]
	return people_needed

def main():
	#sys.stdout = open('A-small-attempt1.out','w')
	sys.stdout = open('A-large.out','w')
	stdin  = open('A-large.in','r')
	#stdin  = open('A-small-attempt1.in','r')
	#stdin  = open('A.small.in','r')
	casos = int(stdin.readline().strip())
	for caso in range(casos):
		inp_str = stdin.readline().strip().split(' ')
		s = [int(c) for c in inp_str[1]]
		s = s[0:int(inp_str[0])+1]
		ans = solve(s)
		print('Case #{0}: {1}'.format(caso+1,ans))

main()
