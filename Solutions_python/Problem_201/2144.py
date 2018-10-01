import bisect

def f(n, k):
	stallGaps = [n]
	for i in range(k-1):
		m = stallGaps[-1]
		stallGaps = stallGaps[:-1]
		if m == 2:
			bisect.insort(stallGaps, 1)
		elif m == 1:
			pass
		else:
			bisect.insort(stallGaps, (m-1)//2)
			bisect.insort(stallGaps, m//2)
	return (stallGaps[-1]//2, (stallGaps[-1]-1)//2)
	
x = int(input())
l = []
for i in range(x):
    l.append([int(x) for x in input().split(" ")])
for i in range(x):
    n, k = l[i]
    maximum, minimum = f(n,k)
    print("Case #%d: %d %d" %(i+1, maximum, minimum))
