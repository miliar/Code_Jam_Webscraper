#Cookie Clicker Alpha

fin = open("B-large.in","r")
fout = open("B-large-out.txt","w")

for i in range(int(fin.readline())):
    line = fin.readline().split()
    for j in range(len(line)):
        line[j] = float(line[j])
    C = line[0]
    F = line[1]
    X = line[2]
    farm = 0.0
    time = 0.0
    while ((C/(farm*F +2) + X/((farm + 1)*F + 2)) < (X/(farm*F + 2))):
            time += (C/(farm*F +2))
            farm += 1.0
    time += (X/(farm*F + 2))
    fout.write("Case #" + str(i + 1) + ": " + str(time) + "\n")

fin.close()
fout.close()
