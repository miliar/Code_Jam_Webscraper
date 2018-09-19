from math import *

fin = open('D-small-attempt1.in','r')
fout = open('d2015sout.txt','w')

T = int((fin.readline()).strip())   # T is the number of test cases

for test in range(T):
    # Write the main program here for each test case
    # test = test number
    # result = the result for the test case
    
    linein = fin.readline().strip().split()
    X,R,C = int(linein[0]),int(linein[1]),int(linein[2])

    result = "GABRIEL"
    if (R*C)%X != 0:
        result = "RICHARD"
    elif X == 3:
        if (R < 2) or (C < 2) or max(R,C) < 3:
            result = "RICHARD"
    elif X == 4:
        if (R < 2) or (C < 2) or max(R,C) < 4 or [R,C] in [[2,4],[4,2]]:
            result = "RICHARD"            
    
    output_str = 'Case #' + str(test+1) + ': ' + str(result) + '\n'
    fout.write(output_str)
    
fin.close()
fout.close()
