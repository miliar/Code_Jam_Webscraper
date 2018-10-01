import sys

def reverse(n, p=0):
	if(n==0):
		return p
	return reverse(n//10, p * 10 + n % 10)

def solve(A,B):
	i = 1
	result = 0

	while(i*i <= B):
		if(i*i >= A):
			if(reverse(i*i) == i*i and reverse(i) == i):
				result += 1
		i += 1
	return result

n = int(input())
for i in range(0,n):
	data = input().split(' ');
	print('Case #'+str(i+1)+': '+str(solve(int(data[0]),int(data[1]))))
