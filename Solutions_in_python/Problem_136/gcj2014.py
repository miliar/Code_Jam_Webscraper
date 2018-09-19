def costs(C, F, i):
    total=float(0)
    for k in range(i):
        total+=C/(2+k*F)
    return total

def getSeconds(C, F, X):
    i=1
    seconds = X/2
    while True:
        if seconds > costs(C, F, i)+X/(2+i*F):
            seconds = costs(C, F, i)+X/(2+i*F)
        else :
            return seconds
        i+=1


fin = open('B-small-attempt0.in')
fout = open('output.out', 'w')

lineNb=0
for line in fin:
    if lineNb==0:
        lineNb+=1
        continue
    numbers = line.strip().split(" ")
    C, F, X = float(numbers[0]), float(numbers[1]), float(numbers[2])
    fout.write("Case #"+str(lineNb)+": "+str(getSeconds(C, F, X))+"\n")
    lineNb+=1

fout.close()

