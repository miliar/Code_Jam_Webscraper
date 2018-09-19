n = 'E:\code\pset1\input.in'
o = 'E:\code\pset1\output.out'

fin = open(n, 'r', 0)
fout = open ( o, 'w', 0)
line = fin.readline()
for gameNumber in range(int(line)):
    line = fin.readline()
    c, f, x = line.split()
    c = float(c)
    f = float(f)
    x = float(x)
    currentTime = x/2.0
    preTime = 0.0
    counter = 0
    while(True):
        preTime = currentTime
        counter += 1
        #for each maximum number of farms:
        time = 0.0
        cp = 2.0
        for numx in range(counter):
            time = time + c/cp
            cp = cp + f
        time += x/cp
        #print time
        currentTime = time
        if currentTime > preTime:
            break
    towrite = 'case #' + str(gameNumber+1) + ': ' + str(preTime)+'\n'
    fout.write(towrite)
fout.close()
fin.close()
    #print preTime
    #print '-----------------------------'
        
        
        