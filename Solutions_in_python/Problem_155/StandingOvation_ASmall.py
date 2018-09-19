inputfile = open("A-large.in",'r')
outputfile = open("output_ALarge.txt",'w')

firstline = inputfile.readline()

counter = 0
while counter<int(firstline):
    inputline = inputfile.readline()
    tokens = inputline.split()
    smax = int(tokens[0])
    sequence = tokens[1]
    
    i = 0
    summ = 0
    minfriend = 0
    while i <= smax:
        summ += int(sequence[i])
        if i + 1 > summ:
            minfriend += (i + 1 - summ)
            summ += 1
        i += 1
    
    #print("Case #"+str(counter+1)+": "+str(minfriend))
    outputfile.write("Case #"+str(counter+1)+": "+str(minfriend))
    outputfile.write("\n")
    counter += 1
    

inputfile.close()
outputfile.close()