file = open("B-large.in", "r")

out = open("B-large.out", "w")

cases = int(file.readline())


def arrayNotDescending(array):
    
    for i in range(len(array)-1):
        if array[i+1] < array[i]:
            return False
    
    return True

for case in range(cases):

    #converts string into integer array
    Number = int(file.readline().replace("\n", ""))
    
    print("serching with number "+str(Number))
    
    
    
    
    while True:
        
        strNr = str(Number)
        
        if arrayNotDescending(list(strNr)):
            print("Last nondescending number: "+strNr)
            out.write("Case #"+str(case+1)+": "+strNr+"\n")
            break
        
        subtract = 1
        #get most right smaller number
        reversedarray = list(strNr)
        reversedarray.reverse()
        print(reversedarray)
        subarray = []
        
        for i in range(len(reversedarray)-1):
            if reversedarray[i] < reversedarray[i+1]:
                #found splitstelle
                subarray = reversedarray[:(i+1)]
                break
        
        subarray.reverse()
        print(subarray)
        substring = "".join(subarray)
        
        print(substring)
        subtract += int(substring)
        
        Number -= subtract
        
        
