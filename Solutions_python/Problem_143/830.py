def solve(A,B,K):

	ans = 0

	for i in range(A):
		for j in range(B):
			if i & j < K:
				ans += 1

	return str(ans)
		

f = open("B-in-small.txt","r")
d = f.read().split("\n")
n = int(d[0])

g = open("B-out-small.txt","w")

for i in range(1,n+1):
	A = int(d[i].split(" ")[0])
	B = int(d[i].split(" ")[1])
	K = int(d[i].split(" ")[2])

	g.write("Case #" + str(i) + ": " + solve(A,B,K) + "\n") 
