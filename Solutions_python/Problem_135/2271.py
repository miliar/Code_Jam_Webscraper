f = open('A-small-attempt3.in')
iter = int(f.readline())
rows = [list(), list(), list(), list()]
for i in range(iter):
    row = int(f.readline())-1
    rows[0] = f.readline()
    rows[1] = f.readline()
    rows[2] = f.readline()
    rows[3] = f.readline()
    #print rows
    #print row
    Set1 = set(rows[row].split())
    row = int(f.readline())-1
    rows[0] = f.readline()
    rows[1] = f.readline()
    rows[2] = f.readline()
    rows[3] = f.readline()
    Set2 = set(rows[row].split())
    #print Set1, Set2
    result = set.intersection(Set1, Set2)
    #print result
    if (len(result) == 1):
        print "Case #"+str(int(i)+1)+":", list(result)[0]
    if (len(result) == 0):
        print "Case #"+str(int(i)+1)+": Volunteer cheated!"
    if (len(result) > 1):
        print "Case #"+str(int(i)+1)+": Bad magician!"
    
