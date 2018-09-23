def nozeros(t):
	i = 0
	while i < len(t) - 1:
		if i < len(t) - 2 and t[i] == t[i+1] and t[i+1] > t[i+2]:
			for j in range(i+1, len(t)):
				t[j] = 9
			t[i] -= 1
			break

		if t[i] > t[i+1]:
			for j in range(i+1, len(t)):
				t[j] = 9
			t[i] -= 1
			j = i
			while j > 0:
				if t[j] < t[j-1]:
					t[j-1] -= abs(t[j]-t[j-1])
				j -= 1
			break
		i += 1
	ans = ''.join(map(str, t))
	return ans

def solve(num):
	if(len(num) == 1):
		return int(num)
	t = list(map(int, list(num)))
	if t.count(0) == 0:
		ans = nozeros(t)
	else:
		while t.count(0) >= 1:
			i = t.index(0)
			j = i
			while j < len(t):
				t[j] = 9
				j += 1
			if i != 0:
				t[i-1] -= 1
			if t[0] == 0: break
		
		ans = nozeros(t)
	return int(ans)

if __name__ == '__main__':
	t = int(input())
	for test in range(1, t + 1):
		num = input()
		print("Case #%d: %d" % (test, solve(num)))