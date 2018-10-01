#author : ash-ishh..

def istidy(num):
	lis = list(map(int,list(str(num))))
	for i in range(len(lis)-1):
		if (lis[i] <= lis[i+1]):
			pass
		else:
			return False
	return True

T = int(input())

for i in range(T):
	N = int(input())
	for elem in range(N,0,-1):
		if istidy(elem):
			print("Case #{} : {}".format(i+1,elem))
			break
