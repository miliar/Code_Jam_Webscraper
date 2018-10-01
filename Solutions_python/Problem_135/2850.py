from sys import stdin

results = ['Bad magician!','Volunteer cheated!'];
num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
 
    r1 = int(stdin.readline().strip())
   
    for i in xrange(4):
        line = stdin.readline()
        if r1 == (i+1):
            row1 = set(line.strip().split(' '))
   
    r2 = int(stdin.readline().strip())
    
    for i in xrange(4):
        line = stdin.readline()
        if r2 == (i+1):
            row2 = set(line.strip().split(' '))

    res = list(row1 & row2) 

    if len(res) == 1:
        print "Case #" + str(case_index) + ": " + res[0]
    elif len(res) > 1:
        print "Case #" + str(case_index) + ": Bad magician!"
    else:
        print "Case #" + str(case_index) + ": Volunteer cheated!"
