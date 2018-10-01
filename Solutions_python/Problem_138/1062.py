import bisect
file = open("D-large.in","r")
out = open("out.txt","w")

numCase = int(file.readline())
line = []
weightN = []
weightK = []
wN = []
wK = []
point = 0
for x in range(1,numCase+1):
    elem = file.readline()
    temp = []
    weightN = map(float,file.readline().split())
    weightK = map(float,file.readline().split())
    weightN.sort()
    weightK.sort()
    wN = list(weightN)
    wK = list(weightK)
    for num in wK:
        if bisect.bisect(wN,num) < len(wN):
            temp.append(bisect.bisect(wN,num))
            wN.pop(bisect.bisect(wN,num))
    y = len(temp)
    for num in weightN:
        if bisect.bisect(weightK, num) < len(weightK):
            weightK.pop(bisect.bisect(weightK, num))
        else:
            break
    z = len(weightK)
    print >> out, "Case #"+str(x)+": "+str(y)+" "+str(z)

out.close()
file.close()
