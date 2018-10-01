#read off input, 

infile = open("A-small-attempt0.in", 'r')
op_file = open('output.txt', 'w+')


num_cases = int(infile.readline())


for case_no in range(num_cases):

    # read off input, taking just the required rows
    a1 = int(infile.readline())
    s1 = []
    for i in range(4):
        if a1 == i+1: s1 = [int(k) for k in ((infile.readline()).split())]
        else: infile.readline()
    a2 = int(infile.readline())
    s2 = []
    for i in range(4):
        if a2 == i+1: s2 = [int(k) for k in ((infile.readline()).split())]
        else: infile.readline()

    # compare rows:
    k = -1
    for i in s1: 
        if i in s2:
	    if k == -1: k = i
            else: k = -2

    # k:: -1: no answer, -2: multiple answer, other: one answer

    

    if k == -1: op_file.write("Case #"+str(case_no+1)+': '+'Volunteer cheated!\n')
    elif k== -2: op_file.write("Case #"+str(case_no+1)+': '+ 'Bad magician!\n')
    else: op_file.write("Case #"+str(case_no+1)+': '+ str(k)+'\n')
    
infile.close()
op_file.close()  
