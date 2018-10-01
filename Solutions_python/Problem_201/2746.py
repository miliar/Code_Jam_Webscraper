import sys

def simulate(N,K):
	occupied = [False]*N
	Ls = [0]*N
	Rs = [0]*N

	for i in range(N):
		Ls[i] = i
		Rs[i] = N-i-1

	for j in range(K):

		items = []

		#print occupied
		#print Ls
		#print Rs

		for i in range(N):
			if occupied[i]:
				continue

			max_s = max( Ls[i], Rs[i] )
			min_s = min( Ls[i], Rs[i] )
			items.append( (-1*min_s, -1*max_s, i ) )

		items.sort()

		selected_id = items[0][2]

		#print selected_id
		occupied[selected_id] = True
		

		for i in range(1, Rs[selected_id]+1):
			Ls[selected_id+i] = i-1

		for i in range(1, Ls[selected_id]+1):
			Rs[selected_id-i] = i-1


	return (items[0][1]*-1, items[0][0]*-1)


inp = open(sys.argv[1],"r")
inp.readline() # skip number of inputs

for i,s in enumerate(inp):
	data = s.strip().split()
	N = int(data[0])
	K = int(data[1])
	y, z = simulate(N,K)
	print "case #%i: %i %i"%( i+1, y, z)