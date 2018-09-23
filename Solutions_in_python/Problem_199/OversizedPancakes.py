
file = "./A-large.in"
file_ans = "./pancakes.out"


sign = {'+': '-', '-': '+'}

with open(file, "r") as f:
	with open(file_ans, "w") as fout:

		T = int(f.readline())
		for t in range(T):
			arr = f.readline().split()
			s = list(arr[0])
			n = len(s)
			k = int(arr[1])
			#print s, k
			#print "s = [%s]" % s

			ret = 0
			for i in range(n-k+1):
				if s[i] == '-':
					for j in range(k):
						s[i+j] = sign[s[i+j]]
					ret += 1


			ok = True
			for i in range(n):
				if s[i] == '-':
					ok = False
					break

			#print s, ret
			sol = str(ret) if ok else "IMPOSSIBLE"
			fout.write("Case #%d: %s\n" % (t+1, sol))
				


