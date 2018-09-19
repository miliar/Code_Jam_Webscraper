from math import *

fin = open('A-large.in','r')
fout = open('a2015lout.txt','w')

T = int((fin.readline()).strip())   # T is the number of test cases

for test in range(T):
    # Write the main program here for each test case
    # test = test number
    # result = the result for the test case
    
    linein = fin.readline().strip().split()
    Smax, sstr = int(linein[0]), linein[1]

    result = 0
    Ncurr = 0
    Scurr = 0
    while len(sstr) != 0:
        result += (Ncurr<Scurr)*(Scurr - Ncurr)
        Ncurr += (Ncurr<Scurr)*(Scurr - Ncurr) + int(sstr[0])
        
        sstr = sstr[1:]
        Scurr += 1
    
    output_str = 'Case #' + str(test+1) + ': ' + str(result) + '\n'
    fout.write(output_str)
    
fin.close()
fout.close()
