f = open('D-large.in','r')
T = int(f.readline().strip())
w = open('outputDeceit1.txt', 'w')
it = lambda x: float(x)

for z in range(T):
	N = int(f.readline().strip())
	A = map(it,f.readline().split())
	B = map(it,f.readline().split())
	A = sorted(A)
	B = sorted(B)
	#Compute the number of weights they can beat on the other side
	A_ind = N*[0]
	B_ind = N*[0]
	A_inc = 0
	B_inc = 0
	while (A_inc < N and B_inc < N):
		if A[A_inc] > B[B_inc]:
			B[B_inc] = A_inc#Set it to the one that it cannot beat
			B_inc += 1
		else:
			A[A_inc] = B_inc
			A_inc += 1
	#Assign the value of N to the weights if they beat all of them
	if A_inc == N:
		while (B_inc < N):
			B[B_inc] = A_inc
			B_inc += 1
	if B_inc == N:
		while (A_inc < N):
			A[A_inc] = B_inc
			A_inc += 1
	#Naomi's strategy: Throw away losers until all of her
	#remaining weights can win something
	A_win = 0
	for i in range(N):
		if A[i] > A_win:#If the weight beats the current opposition in indice
			A_win += 1
	#Naomi plays fairly
	#Then Ken wins using the lowest weight possible
	B_win = 0
	for i in range(N):
		if B[i] > B_win:#If the weight beats the current opposition in indice
			B_win += 1
	w.write("Case #" + str(z+1) + ": " +str(A_win)+ " " + str(N-B_win)+ "\n")
