import pprint

f = open('A-large.in', 'r')
cases = f.readline()
fWrite = open('A-large.out', 'w')
           

for i in range(int(cases)):
    dSnappers = []
    aData = f.readline().split()
    snapperCount = aData[0]
    snapCount = aData[1]
    light = 'OFF'
    square = 2**int(snapperCount)
    if (int(snapCount) + 1) % square == 0:
        light = 'ON'
    strOut = "Case #"+str(i+1)+': '+light+'\n'

    fWrite.write(strOut);
    print strOut

f.close()
fWrite.close()
