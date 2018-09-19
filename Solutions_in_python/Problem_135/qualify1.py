fp=open("A-small-attempt4.in",'r')
fo=open("A-small-attempt4.out","w")
numberOfTest=fp.readline()
for testNumber in range(int(numberOfTest)):
    if(testNumber>0):
        fo.write("\n")
    answer1=fp.readline()
    arrangement1={}
    for row in range(4):
        line=fp.readline()
        if(row==int(answer1)-1):
            line=line.replace("\n","")
            arrangement1[0]=line.split(" ")

        
    answer2=fp.readline()
    arrangement2={}
    for row in range(4):
        line=fp.readline()
        if(row==int(answer2)-1):
            line=line.replace("\n","")
            arrangement2[0]=line.split(" ")

    numbers=0
    count=0
    for i in range(4):
        for j in range(4):
            if arrangement1[0][i]==arrangement2[0][j]:
                numbers=arrangement2[0][j]
                count=count+1
 
    if count==1:
        fo.write("Case #"+str(testNumber+1)+": "+numbers)
        #print "Case #"+str(testNumber+1)+": "+numbers
    elif count==0:
        fo.write("Case #"+str(testNumber+1)+": Volunteer cheated!")
        #print "Case #"+str(testNumber+1)+": Volunteer cheated!"
    else:
        fo.write("Case #"+str(testNumber+1)+": Bad magician!")
        #print "Case #"+str(testNumber+1)+": Bad magician!"


        
            
        
fo.close()        
fp.close()
