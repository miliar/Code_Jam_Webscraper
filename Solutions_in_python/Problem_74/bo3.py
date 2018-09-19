input1 = open(r"c:\googleCode\a-large.in")
output1 = open(r"c:\googleCode\botlarge.txt", 'w')
lines = input1.readline()
testC = int(lines.strip())
caseN = 1
lines = input1.readline()

while lines !='':
    totalButton = (lines.strip()).split(' ')
    buttonN = int(totalButton.pop(0))
    totalT=0
    ot=bt =0
    op=bp =1
    OE = [0]
    BE =[0]
    
    if buttonN !=0:
        count =0
        while count < buttonN:
            #print totalButton
            X = totalButton.pop(0)
            Y = int(totalButton.pop(0))
            if X =='O':
                ot = abs(Y-op)
                op=Y
                ot +=OE[-1]
                if ot <=BE[-1]:
                    OE.append(BE[-1]+1)
                else:
                    OE.append(ot+1)
            else:
                bt =abs(Y-bp)
                bp=Y
                bt +=BE[-1]
                if bt <=OE[-1]:
                    BE.append(OE[-1]+1)
                else:
                    BE.append(bt+1)
            count +=1
        totalT = BE[-1]
        if BE[-1]<OE[-1]:
            totalT =OE[-1]
    result ="Case #"+str(caseN)+": "+ str(totalT)+'\n'
    output1.write(result)
    print (result)
    caseN +=1
    lines = input1.readline()

output1.close()
input1.close()
