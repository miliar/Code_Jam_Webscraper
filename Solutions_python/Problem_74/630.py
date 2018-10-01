fin = file("A-large.in", "rU")
fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()
    #print line
    opos = 1
    bpos = 1
    total = 0
    prev = ''
    freetime = 0
    for j in xrange(1, len(line), 2):
        if line[j] == 'O':
            if prev == 'B': #can use freetime to move
                total += max(abs(int(line[j+1])-opos) - freetime + 1, 1)
                freetime = max(abs(int(line[j+1])-opos) - freetime + 1, 1)
            else:
                total += abs(int(line[j+1])-opos) + 1
                freetime += abs(int(line[j+1])-opos) + 1
            prev = 'O'
            opos = int(line[j+1])
        elif line[j] == 'B':
            if prev == 'O': #can use freetime to move
                total += max(abs(int(line[j+1])-bpos) - freetime + 1, 1)
                freetime = max(abs(int(line[j+1])-bpos) - freetime + 1, 1)
            else:
                total += abs(int(line[j+1])-bpos) + 1
                freetime += abs(int(line[j+1])-bpos) + 1
            prev = 'B'
            bpos = int(line[j+1])
    strout = "Case #" + str(i+1) + ": " + str(total) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
