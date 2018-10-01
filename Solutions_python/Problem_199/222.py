#!/usr/bin/python
 
import math
from Queue import PriorityQueue
#from decimal import *
#import fractions 
#getcontext().prec = 50
#_modulo = 10**9 + 7


def lower_bound(nums, target):
	l, r = 0, len(nums) - 1
	while l <= r:
		mid = l + (r - l) / 2
		if nums[mid] >= target:
			r = mid - 1
		else:
			l = mid + 1
	return l
	
def upper_bound(nums, target):
	l, r = 0, len(nums) - 1
	while l <= r:
		mid = l + (r - l) / 2
		if nums[mid] > target:
			r = mid - 1
		else:
			l = mid + 1
	return l
		
def main():
	import sys

	T = int(raw_input().strip())
	
	for t in xrange(T):
		S, K = raw_input().strip().split()
		
		K = int(K)
		swap = []
		
		for i in xrange(len(S)):
			
			n_swap = len(swap) - lower_bound(swap,i-K+1)
			if ( (n_swap%2 ==0) and (S[i] == '-'))  or ( (n_swap%2 ==1) and (S[i] == '+')):
				swap.append(i)
				
		
		#print swap
		
		forbid = len(swap) - upper_bound(swap,len(S)-1-K+1)
		
		
		if forbid != 0:
			sol = 'IMPOSSIBLE'
		else:
			sol = str(  len(swap) )
			
		print "Case #" + str(t+1) + ": "+ sol
	
	#(N, Q) = map(int,raw_input().strip().split())
	#ww= [""]*N
	#qq = PriorityQueue()
	
	
	
	
if __name__ == "__main__":
	
	#import time
	#the_start_time = time.time()
	main()
	
	
	#A = [3,5,6]
	
	#print lower_bound(A,5)
	#print upper_bound(A,5)
	
	#print time.time() - the_start_time
	
	
		
	
