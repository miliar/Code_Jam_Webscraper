import operator
import functools

t = int(input())

EPS = 1e-9

for case in range(1,t+1):
	n,k = [int(x) for x in input().split()]
	U = float(input())
	arr = [float(x) for x in input().split()]
	arr = sorted(arr)
	# print(arr)

	for i in range(len(arr)):
		ned = arr[i+1] - arr[i] if i+1 < len(arr) else 1.0
		# print("ned",ned)
		inc = U/(i+1) if ned*(i+1) > U - EPS else ned
		# print("inc",ned)
		U -= inc*(i+1)
		for j in range(i+1):
			arr[j] += inc
		if U < EPS:
			break
	# print(arr)

	ans = functools.reduce(operator.mul, arr)
	print('Case #%d: %.10f' % (case, ans))
