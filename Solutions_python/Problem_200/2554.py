lis = []
fOut = open('out2.txt','w')
for i in open('B-large.in'):
    lis.append(i.strip())

caseSize = int(lis[0])

solList = []

for case in lis[1:caseSize+1]: ###FOR EACH CASE
    number = int(case)
    print('Number to analyse ' + str(number))
    
    flag = True
    

    listOfDigits = list(str(number))
    olNumber = number
    
    for pos in reversed(range(1,len(listOfDigits))): #Moving from right to left
        if (int(listOfDigits[pos]) - int(listOfDigits[pos-1])) < 0:  #If theres been an increase                      
            listOfDigits[pos-1] = int(listOfDigits[pos-1]) - 1
            #everything from listOfDigits[pos:] onwards needs to become a 9.
            a = listOfDigits
            a[pos:] = [9] * len(a[pos:])
            #print(a)
        else:
            a = listOfDigits
            
    sol = []
    for val in a:
        sol.append(str(val))

        
    if sol[0] == '0': #picks up zeroes at the start of the string
        del sol[0]
    if len(case) == 1:
        sol = case
    solList.append(''.join(sol))


for val in range(0,len(solList)):
    fOut.write("Case #" + str(val+1) + ": " + str(solList[val]) + "\n")
fOut.close()
