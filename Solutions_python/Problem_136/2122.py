import sys

cases = sys.stdin.readline()
cases = int(cases)

data1 = []
data2 = []

def work(idx):
	in1 = sys.stdin.readline()
	in1 = map(lambda y:float(y), in1.strip().split())
	C ,F ,X = in1[0],in1[1],in1[2]

	databuild = []

	currentmin = X/2.0
	i=0
	while True:
		speed = 2.0;
		if i == 0:
			buildtime = 0.0
		else:
			speed = 2.0 + F * (i-1)
			buildtime = C/speed
			buildtime += databuild[ i - 1 ]
			speed += F
		databuild += [ buildtime ]

		totaltime = buildtime + X/speed
		#print idx,totaltime, buildtime,speed #debug

		if totaltime > currentmin:
			print "Case #%d: %.7f" % (idx, currentmin);
			return
		currentmin = totaltime
		i += 1

	print "Case #%d: %.7f" % (idx, currentmin);

for i in range(cases):
	work(i+1)


