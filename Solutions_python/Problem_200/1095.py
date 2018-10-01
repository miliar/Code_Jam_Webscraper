import sys
from sys import argv

def flip(n):
	l = len(n)
	if n[0] > n[1]:
		n[0] = int(n[0]) - 1 
		n[1:] = [9] * ( l - 1 )
	return n

def sort(n):
	if len(n) < 2 :
		return n
	new_n = 0
	if n[0] <=  n[1]:
		n[1:] = sort(n[1:])
	n = flip(n)
	return n

T = int(input())
for i in range(0, T):
	n = list(map(int, input().strip()))
	print("Case #",i+1,": ",sep="",end="")
	print(int(''.join(str(i) for i in sort(n))))
