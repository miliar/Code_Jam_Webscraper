import sys
import itertools

filename = "a.in"
outfilename = "a.out"
if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    outfilename = sys.argv[2]
inputfile = file(filename, 'rb')
outputfile = file(outfilename, 'wb')

case = 1

lines = inputfile.readlines()
testcases = int(lines[0].strip())
for line in lines[1:]:
    if len(line.strip()) == 0:
        continue
    A = int(line.strip().split(' ')[0])
    B = int(line.strip().split(' ')[1])
    K = int(line.strip().split(' ')[2])
    Krange = range(0,K)
    Arange = range(0,A)
    Brange = range(0,B)
    wincount = 0

    for machine1 in Arange:
        for machine2 in Brange:
            if (machine1&machine2) < K:
#            if Krange.count(machine1&machine2) > 0:
                wincount += 1

    outputfile.write("Case #%i: %i\r\n" % (case, wincount))
    print "Case #%i: %i" % (case, wincount)
    case += 1
    
inputfile.close()
outputfile.close()
