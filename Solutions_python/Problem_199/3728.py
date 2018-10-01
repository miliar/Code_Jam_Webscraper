


f = open('C:\Users\HabibR\Desktop\google code jam\A-large.in', 'r')
n = int(f.readline())

output = open('C:\Users\HabibR\Desktop\google code jam\outputLarge.txt', 'w')

allTrials = []
#for i in range(n):
#    allTrials.append(raw_input())


#allTrials.append("300 300")
#allTrials.append("500 1001")
#allTrials.append("400 1005")
#allTrials.append("200 207")


#allTrials.append("---+-++- 3")
#allTrials.append("+++++ 4")
#allTrials.append("-+-+- 4")

for i in range(n):
    allTrials.append(f.readline())


for i in range(len(allTrials)):
    data = []
    dataBeforeParse  = allTrials[i].split(" ")
    for j in dataBeforeParse[0]:
        if(j == "+"):
            data.append(True)
        else:
            data.append(False)
        
    step = int(dataBeforeParse[1])
    
    smallestSteps = 0
    
    for m in range(len(data)):
        if(data[m] == False):
            if(len(data)-m < step):
                smallestSteps = -1
                break;
            else: #flip the next n steps
                for k in range(step):
                    data[m+k] = not data[m+k]
                smallestSteps+=1
    if smallestSteps==-1:
        smallestSteps = "Impossible"
    
    output.write( "Case #"+str(i+1)+": "+str(smallestSteps) +"\n"  )          
    print "Case #"+str(i+1)+": "+str(smallestSteps) +"\n" 


f.close()
output.close()



