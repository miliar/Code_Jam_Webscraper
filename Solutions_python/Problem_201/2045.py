from collections import deque

def get_ls_rs(data, i):
	l, r = i-1, i+1
	while not data[l]:
		l-=1
	while not data[r]:
		r+=1
	return i-l-1, r-i-1

def minnegmax(a, i):
	return -min(a), -max(a), i

import operator
def best(data):
	li = [minnegmax(get_ls_rs(data, i),i) for i, e in enumerate(data) if not e]
	#print(li)
	li = sorted(li)
	#print(li)
	return li[0]
	
for t in range(1, int(input()) + 1):
	i,j = tuple(map(int,input().split()))
	data = deque(0 for e in range(0,i))
	data.append(1)
	data.appendleft(1)
	out = None
	for e in range(1,j+1):
		out = best(data)
		data[out[2]] = 1
	print("Case #{}: {} {}".format(t, -out[1], -out[0]))