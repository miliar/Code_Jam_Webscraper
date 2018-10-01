import math
pi = math.pi
f = open("A.in")
g = open("Aout.txt","w")
T = int(f.readline())
def cals(A):
	S = A[0] ** 2 + 2 * A[0] * A[1]
	return S
for t in range(T):
	case = "Case #" + str(t + 1) + ": "
	N,K = map(int,f.readline().split())
	pan = [list(map(int,f.readline().split())) for i in range(N)]
	pan.sort(key = lambda x: (- x[0], - x[1]))
	Slist = []
	for p in range(N):
		ans = cals(pan[0]) * pi
		pan.pop(0)
		if len(pan) + 1 < K:
			break
		pan2s = [pan[i][0] * 2 * pan[i][1] * pi for i in range(N - p - 1)]
		if t < 3:
			print(pan2s)
		pan2s.sort(key = lambda x:-x)
		sokumen = sum(pan2s[:K - 1])
		ans += sokumen
		Slist.append(ans)
	g.write(case + str(max(Slist)) + "\n")

