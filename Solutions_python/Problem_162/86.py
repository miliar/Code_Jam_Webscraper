T = int(raw_input())
f = open('out2.txt', 'w')
cas = 0
while T > 0:
	T -= 1
	n = int(raw_input())
	now = 1
	cnt = 1
	while now < n:
		need = min(now * 10 - 1, n - 1)
		snow = str(need)
		# print need, now
		nowres = need - now
		for i in xrange(len(snow)):
			for j in xrange(int(snow[i])):
				tmp = j * (10 ** (len(snow) - i - 1))
				if i != len(snow) - 1:
					tmp = int(snow[i + 1::]) + tmp
				rsnow = snow[::-1]
				ri = len(snow) - i - 1
				tmp += int(rsnow[ri::]) - j * (10 ** i)
				if tmp < nowres:
					nowres = tmp
		now = need + 1
		cnt += nowres + 1
	cas += 1
	# print cnt
	f.write("Case #" + str(cas) + ": " + str(cnt) + '\n')
