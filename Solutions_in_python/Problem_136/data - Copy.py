fin = open("B-large.in", 'r')
#fin = open("test.txt", 'r')
fout= open("out.txt", 'w')




testCaNum= int(fin.readline().strip())
for testCa in range(1, testCaNum +1):
    curat = 2.0
    fch = fin.readline().strip().split()
    time = 0
    for num in range(3):
        fch[num]=float(fch[num])
    
    mor = True    
    while mor:
        i = fch[0]/curat + fch[2]/(curat + fch[1])
        j = fch[2]/curat
        if (j > i):
            time = time + fch[0]/curat
            curat = curat + fch[1]
        else:
            time = time + j
            mor = False
            
        
    
    
    fout.write("Case #"+str(testCa)+": %.7f"%time+"\n")
        
fin.close()
fout.close()
