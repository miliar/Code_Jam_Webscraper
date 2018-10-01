txt = [line.strip() for line in open('input.txt').readlines()]
output = open('output.txt','w')
caseCount = int(txt[0])

def solver(costOfFarm,farmProd,numOfCookies):
    newTimeFin = numOfCookies/2.0        
    farms= 0.0
    rate =  costOfFarm/2.0
    timeFin = float('inf')    
    while newTimeFin < timeFin:
        timeFin = newTimeFin
        farms +=1
        newRate = farmProd*farms + 2.0 
        newTimeFin = numOfCookies/newRate + rate
        rate += costOfFarm/newRate
    return timeFin
        

for ind in range(caseCount):
    cost,fprod,target = txt[ind+1].split()
    out = str(solver(float(cost),float(fprod),float(target)))
    output.write('Case #'+ str(ind+1)+': '+out+'\n')
