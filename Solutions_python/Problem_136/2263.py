inputs = open('codejamB.txt', 'r')
inputlines=[]
for line in inputs:
    inputlines.append(line)
T = int(inputlines[0].strip())

for i in range(1, T+1):
    line = inputlines[i].split(' ')
    [c, f, x] = [float(line[0].strip()), float(line[1].strip()), float(line[2].strip())]
    t=0
    k=0
    while( x/(2+k*f) > x/(2+(k+1)*f) + c/(2+k*f) ):
        t+=(c/(2+k*f))
        k+=1
    t+=(x/(2+k*f))
    #print k
    print "Case #"+str(i)+": "+str(t)
