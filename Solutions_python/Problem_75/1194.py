import sys

testfile = sys.argv[1]

infile = open(testfile,'r')

count = int(infile.readline())

for i in range(1,count+1):

    line = infile.readline()
    line = line.strip()
    line = line.split()

    combine = {}

    if line[0] != "0":
        num = int(line[0])
        line.pop(0)
        for j in range(0,num):
            c = line[0]
            combine[c[:2]] = c[2]
            line.pop(0)
    elif line[0] == "0":
        line.pop(0)

    clear = []

    if line[0] != "0":
        num = int(line[0])
        line.pop(0)
        for j in range(0,num):
            clear.append(line[0])
            line.pop(0)
    elif line[0] == "0":
        line.pop(0)

    final = []

    if line[0] != "0":
        num = int(line[0])
        line.pop(0)
        line = list(line[0])

        for j in range(0,num):
            #add letter to final list
            final.append(line[0])
            line.pop(0)
            
            #check if combine
            if ''.join(final[-2:]) in combine: 
                #print ''.join(final[-2:])
                elem = combine[''.join(final[-2:])] 
                final.pop(len(final)-1)
                final.pop(len(final)-1)
                final.append(elem)
            elif ''.join(reversed(final[-2:])) in combine:
                #print ''.join(reversed(final[-2:])) 
                elem = combine[''.join(reversed(final[-2:]))] 
                final.pop(len(final)-1)
                final.pop(len(final)-1)
                final.append(elem)

            #check if clear
            for k in range(0,len(final)-1):
                if final[k] + str(final[-1:][0]) in clear:
                    final = []
                    break
                elif str(final[-1:][0]) + final[k] in clear:
                    final = []
                    break
    
    print "Case #"+str(i) + ": [" + ", ".join(final) + "]"


    
            
