import argparse

def ConvertTime(t):
	newTime = str(t)
	intPart = newTime.split(".")
	decPart = intPart[1]
	intPart = intPart[0]
	if len(decPart)!=7:
		decPart+="0"*(7-len(decPart))
	return intPart+"."+decPart

def Calculate(C,F,X):
	cps = 2
	cookieCount = 0
	totalTime = 0
	solveTime = X/cps
	while True:
		prevTime = solveTime
		totalTime += C/cps
		cps+=F
		solveTime =  totalTime + (X/cps)
		if solveTime>=prevTime:
			return ConvertTime(round(prevTime,7))

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", help="Enter the filename")
args = parser.parse_args()
filename = args.filename
f = open(filename,'r')
N = int(f.readline().split("\n")[0])
fout = open("output.txt",'w')
for i in range(1,N+1):
    temp = f.readline().split("\n")[0].split(" ")
    C,F,X = [float(t) for t in temp]
    fout.write("Case #"+str(i)+": "+Calculate(C,F,X)+"\n")
fout.close()