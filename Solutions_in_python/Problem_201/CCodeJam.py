def calculate(case):
    array= case.split()
    people=array[1]
    array.remove(people)
    people=int(people)
    i=0
    tempMax=0
    tempMin=0
    while i<int(people):
        j=0
        tempSpace=0
        while j<len(array):
            if tempSpace<int(array[j]):
                tempSpace=float(array[j])
            j+=1
        if(tempSpace-1)%2!=0:
            tempMax=int((tempSpace-1)/2+0.5)
            tempMin=int((tempSpace-1)/2-0.5)
        else:
            tempMax=int((tempSpace-1)/2)
            tempMin=int(tempMax)
        array.append(str(tempMax))
        array.append(str(tempMin))
        array.remove(str(int(tempSpace)))
        i+=1
    return str(str(tempMax)+" "+str(tempMin))
            
            
        


j=0
f = open('C:/Users/Vedat/Desktop/VAK/Coding/Python/Codejam 8.4.17/C-small-1-attempt0.in','r')
numberOfCases=f.readline()
numberOfCases = int(numberOfCases)
while j<numberOfCases:
    case=f.readline()
    print('Case #'+str(j+1)+': '+ str(calculate (case)))
    j+=1
