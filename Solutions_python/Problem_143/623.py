
output = []
tc = int(raw_input())
for t in range(tc):
	count = 0
	curInput = raw_input().split()
	A = int(curInput[0])
	B = int(curInput[1])
	K = int(curInput[2])
	for i in range(0, A):
		for j in range(0, B):
			if (i & j < K):
				count = count + 1

	output.append('Case #' + str(t+1) + ': '+ str(count))

for t in range(tc):
	print output[t]
