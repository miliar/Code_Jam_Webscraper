import sys

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

T = int(in_file.readline())

for i in range(T):
	R = 2
	time = float(0.0)
	tmp = in_file.readline().split()
	C, F, X = float(tmp[0]), float(tmp[1]), float(tmp[2])
	while ( (X/(R+F)) + C/R < X/R ):
		time += C/R
		R += F
	time += X/R
	out_file.write('Case #{0}: {1:.7f}\n'.format(i+1, time))

in_file.close()
out_file.close()
