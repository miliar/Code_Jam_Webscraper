fout = open("Bout.txt",'w')
fout.write('')
fout.close()

fin = open('B-large.in')
N = int(fin.readline())

for i in range(N):
	#read in params:
	params = fin.readline().split()
	C = float(params[0])
	F = float(params[1])
	X = float(params[2])

	#initial rate and time:
	rate = 2
	t_total = 0

	#do while buying a farm is faster:
	while True:
		t_nofarm = X/rate #total time without next farm
		t_farm = C/rate + X/(rate+F) #total time with next farm

		if t_farm < t_nofarm:
			#add time taken to buy farm and update rate:
			t_total+=C/rate
			rate+=F
		else:
			#add time taken to reach X cookies then exit loop:
			t_total+=t_nofarm
			break

	#write to output file:
	fout = open("Bout.txt",'a')

	fout.write('Case #%d: %.7F\n'%(i+1, t_total))

	fout.close()

fin.close


