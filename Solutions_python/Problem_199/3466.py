from __future__ import print_function
t = int(input())

arr = []

def flip(b):
	if(arr[b] == '-'): 
		arr[b] = '+'
	else:
		arr[b] = '-'
def flipk(b, k):
	#print(k)
	#print(b)
	for i in range(b-k+1, b+1):
		#print(i)
		flip(i)
def isBasem(arr, i, k):
	for j in range(i, i+k):
		if(arr[j] == '+'):
			return False
	return True
def isBasep(arr, i, k):
	for j in range(i, i+k):
		if(arr[j] == '-'):
			return False
	return True
def pr(arr):
	for i in range(0, len(arr)):
		print(arr[i], end = '')
	print()
for ti in range(1, t+1):
	s = input().split(' ')
	k = int(s[1])
	s = s[0]
	steps = 0
	arr = []
	for i in range(0, len(s)):
		arr.append(s[i])
	j = len(arr)-1
	while(j >= k):
		# print(j)
		if(arr[j] == '-'):
			#pr(arr)
			#print(j)
			flipk(j, k)
			#pr(arr)
			steps = steps + 1
		j = j-1
		#pr(arr)
	if(isBasem(arr, 0, k)):
		steps = steps + 1
		print("Case #" + str(ti) + ": " + str(steps))
	elif(isBasep(arr,0,k)):
		print("Case #" + str(ti) + ": " + str(steps))
	else:
		print("Case #" + str(ti) + ": IMPOSSIBLE")
	
	



