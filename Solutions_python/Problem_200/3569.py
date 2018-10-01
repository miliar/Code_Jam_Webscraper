lines = [line.rstrip('\n') for line in open('B-large.in')]

T = int(lines[0])
count = 0  

f = open('tidy2.out', 'w')

for k in range(1, T+1):
	num = lines[k]
	ans = num

	final_done = False
	while (not final_done):
		i = 1
		prev = int(ans[0])
		done = False
		while (i < len(num) and not done):
			curr = int(ans[i])
			if (prev > curr):
				ans = ans[0:i-1] + str(prev - 1) + ans[i:]
				for j in range(i, len(num)):
					ans = ans[0:j] + '9' + ans[j+1:]
				done = True
			i = i + 1
			prev = curr
		if (not done):
			final_done = True

	while (len(ans) > 1 and ans[0] is '0'):
		ans = ans[1:]

	if (k < T):
		f.write("Case #" + str(k) + ": " + str(ans) + "\n");
	else:
		f.write("Case #" + str(k) + ": " + str(ans));