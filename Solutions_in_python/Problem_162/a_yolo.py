N    = int(10E6)
yolo = [0] * N

def reverse(i):
	return int(str(i)[::-1])

def presolve():
	for i in xrange(1, N):
		r = reverse(i)
		if i % 10 == 0 or r >= i:
			yolo[i] = 1 + yolo[i - 1]
		else:
			yolo[i] = 1 + min(yolo[r], yolo[i - 1])
		
def solve(n):
	return yolo[n]

presolve();
n = int(raw_input())
i = 0

while i < n:
	i += 1
	x = int(raw_input())
	print('Case #{}: {}'.format(i, solve(x)))