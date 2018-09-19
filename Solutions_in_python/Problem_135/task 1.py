infile = open('input.txt','r')
outfile = open('output.txt','w')
lines = infile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
n = int(lines[0])
for i in range(n):
    k = int(lines[1+i*10])
    values = lines[1+i*10 + k].split()
    k = int(lines[6+i*10])
    val = lines[6+i*10 + k].split()
    result = []
    for j in values:
        if j in val:
            result = result + [j]
    if len(result) > 1:
        print "Case #"+str(i+1)+": Bad magician!"
        outfile.write("Case #"+str(i+1)+": Bad magician!\n")
    elif len(result) < 1:
        print "Case #"+str(i+1)+": Volunteer cheated!"
        outfile.write("Case #"+str(i+1)+": Volunteer cheated!\n")
    else:
        print "Case #"+str(i+1)+": "+result[0]
        outfile.write("Case #"+str(i+1)+": "+result[0]+'\n')
