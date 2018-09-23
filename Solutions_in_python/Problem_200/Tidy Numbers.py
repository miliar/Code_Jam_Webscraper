datafile = str(input("Please enter your file name: "))
with open (datafile, 'r') as datafile:
    data = datafile.read()
ListofData = list(data)
ListofData = list(data.split())
TList = []
i=0
Equal = False
print(ListofData)
print(len(ListofData))

y = 0
T = int(ListofData[0])    
for j in range(1, T+1):
    N = int(ListofData[j])
        
    global NList
    NList= list(str(N))
    print(NList)
    x = len(NList)
    for i in range (0, x-1):
        #if NList[y]==NList[y+1]:
            #print ("Equal")
            #Equal = True
        #else:
            #Equal = False
            #break
            
        if int(NList[x-1])== int(NList[x-2]) and int(NList[0])<=int(NList[1]):
            break
        elif int(NList[0])== int(NList[1]) and int(NList[0])<=int(NList[x-1]):
            break
            
        elif int(NList[i])>=int(NList[i+1]):
            NList[i] = int(NList[i])-1
            print(NList)
            for i in range (1, x):
                if NList[i] == "0":
                    NList[i]= 9
                    #NList[i+1]=9
                    print(NList)
                else:
                    #NList[i]= int(NList[i])-1
                    NList[i] = 9
                    
                    print(NList)
                    print("Section 1")
        N= ""
        for i in range (0, len(NList)):
            N = str(N) + str(NList[i])


            
        while(int(NList[x-1])<int(NList[x-2])):
            N =int(N)-1
            NList = list(str(N))
            x = len(NList)
            print("Section 2")
            print(NList)
        y = y+1        
    N = ""
    if NList[0]== 0:
        NList.remove(NList[0])
    for i in range (0, len(NList)):
        N = str(N) + str(NList[i])
    print(N)
    
    filename = open("results.txt", 'a')
    filename.write("Case #" + str(j) + ": " + N)
    filename.write("\n")
    filename.close()


        
