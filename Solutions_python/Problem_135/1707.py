def run(FILE):
    infile = open(FILE,'r')
    outfile = open('magic.out','w')
    line1 = infile.readline()
    T = int(line1.strip('\n'))
    for i in range(T):
        r1 = int((infile.readline()).strip('\n'))
        a1 = []
        for j in range(4):
            ln = infile.readline()
            ln = ln.strip('\n').split(' ')
            a1.append(ln)
        r2 = int((infile.readline()).strip('\n'))
        a2 = []
        for j in range(4):
            ln = infile.readline()
            ln = ln.strip('\n').split(' ')
            a2.append(ln)
        count = 0
        res = 0
   
        for k in a1[r1 - 1 ]:
            if k in a2[r2 - 1]:
                count += 1
                res = k
        if count == 1:
            outfile.write('Case #' + str(i+1) + ': ' + str(res) +'\n')
        if count > 1:
            outfile.write('Case #' + str(i+1) + ': ' + 'Bad magician!' + '\n')
        if count == 0:
            outfile.write('Case #' + str(i+1) + ': ' + 'Volunteer cheated!' + '\n')
    infile.close()
    outfile.close()
