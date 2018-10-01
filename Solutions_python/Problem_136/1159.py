

f = open('input.txt', 'r')

numCases = int(f.readline())
Cs = [None]*numCases
Fs = [None]*numCases
Xs = [None]*numCases
for case in range(numCases):
	Cs[case], Fs[case], Xs[case] = f.readline().split()
	Cs[case] = float(Cs[case])
	Fs[case] = float(Fs[case])
	Xs[case] = float(Xs[case])
	case+=1
f.close()

out = open('output.txt','w')
for case in range(numCases):
	time = 0.0
	rate = 2.0
	while (Xs[case]/rate > Cs[case]/rate + Xs[case]/(rate+Fs[case])):
		time += Cs[case]/rate
		rate +=Fs[case]
	time+=Xs[case]/rate
	out.write("Case #{0}: {1}\n".format(case+1,time))
out.close()
	
