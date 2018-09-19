#4
#3 1 5 15 13 11
#3 0 8 23 22 21
#2 1 1 8 0
#6 2 8 29 20 8 18 18 21
#Case #1: 3
#Case #2: 2
#Case #3: 1
#Case #4: 3


f = open('input', 'r')
fw = open('output', 'w')
len = f.readline()
#print len.rstrip()
i=0
for x in range(int(len)):
    i+=1
    line = f.readline()
    line = line.rstrip()
    x = line.split()
    N= int(x[0])   #number of googlers
    S = int(x[1])  # Num of surprising
    p = int(x[2])  #Judged this high
    r= x[3:]
    #print N
    #print S
    #print p
    #print r
    higher = 0
    for j in r:
        j = int(j)
        if p > j:
            continue

        elif (p + p + p -2) <=j:
            higher +=1
            #print 'Yes ' + str(p) + '-' + str(j)
        elif (p + p + p -4) <= j and S > 0:
            S-=1
            higher+=1
            #print 'Surprising Yes ' + str(p) + '-' + str(j)
        #print str(j / 3)
        #print j





    #print 'Case #'+str(i)+': '+line
    fw.write( 'Case #'+str(i)+': '+str(higher)+'\n')
