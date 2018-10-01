__author__ = 'christos'

fin = open("in.txt", "r")
fout = open("out.txt", "w")
Tn = int(fin.readline())

for case in range(1, Tn+1):
    line = fin.readline()
    line = line.split()
    s_max = int(line[0])
    n = 0
    claps = 0
    for i in range(s_max+1):

        if claps < i:
            tempN = i - claps
            n += tempN
            claps += tempN
        claps += int(line[1][i])

    fout.write('Case #' +str(case) +': ' + str(n) + "\n")
