from collections import deque
from copy import deepcopy

def flip_char(ch):
	if ch == '+':
		return '-'
	elif ch == '-':
		return '+'
	else:
		raise
		

def flip(s, index, k):
	return s[:index] + ''.join([flip_char(ch) for ch in s[index:index+k]]) + s[index+k:]
	
def are_all_pancakes_happy(pancakes):
	return '-' not in pancakes
	
def get_number_of_flips(pancake_pattern, k):
	if '-' not in pancake_pattern:
		return 0
	q1, q2 = deque(), deque()
	pancake_set = set()
	pancake_set.add(pancake_pattern)
	q1.append(pancake_pattern)
	level = 1
	#import pdb
	#pdb.set_trace()
	while q1:
		node = q1.popleft()
		for idx in range(len(node)- k + 1):
			flipped_pancakes = ''		
			try:
				flipped_pancakes = flip(node, idx, k)
			except:
				return "IMPOSSIBLE"
			if are_all_pancakes_happy(flipped_pancakes):
				return level
			elif flipped_pancakes not in pancake_set:
				q2.append(flipped_pancakes)
				pancake_set.add(flipped_pancakes)
		if not q1:
			level += 1
			q1 = q2
			q2 = deque()
	return 'IMPOSSIBLE'		
				
				
def main():
	for test in range(int(raw_input())):
		pancake,k = raw_input().split(' ')
		k = int(k)
		print "Case #"+ str(test+1)+":",get_number_of_flips(pancake, k)

main()		
		