
fo = open("A-small-attempt5.in", "r")
f = open("A-small-attempt5.out", "w")
lines=fo.readlines()
cases = int(lines[0])

for n in range(0, cases):
    
    array1 = [0]*16
    array2=[0]*16

    input1 = int(lines[10*(n)+1])
    input2 = int(lines[10*(n)+6])
    
    firstrow1 = lines[10*n+2]
    firstrow2 = lines[10*n+3]
    firstrow3=lines[10*n+4]
    firstrow4=lines[10*n+5]
    secondrow1=lines[10*n+7]
    secondrow2=lines[10*n+8]
    secondrow3=lines[10*n+9]
    secondrow4=lines[10*n+10]
    
    
    for i in range(0,4):
        temp = firstrow1.split()
        array1[i] = temp[i]
        
    for i in range(0,4):
        temp = firstrow2.split()
        array1[i+4] = temp[i]
        
    for i in range(0,4):
        temp = firstrow3.split()
        array1[i+8] = temp[i]
        
    for i in range(0,4):
        temp = firstrow4.split()
        array1[i+12] = temp[i]
        
        
    for i in range(0,4):
        temp = secondrow1.split()
        array2[i] = temp[i]
        
    for i in range(0,4):
        temp = secondrow2.split()
        array2[i+4] = temp[i]
        
    for i in range(0,4):
        temp = secondrow3.split()
        array2[i+8] = temp[i]
        
    for i in range(0,4):
        temp = secondrow4.split()
        array2[i+12] = temp[i]



    switch = 0
    solution = 0

    
    for x in range(4*(input1-1), 4*input1):
        for y in range(4*(input2-1), 4*input2):
    
            if array1[x]==array2[y]:
                if switch == 0:
                    switch=1
                    solution = array1[x]
                else:
                    switch=2

  
    if n != 0:
        if switch == 0:
            f.write("\nCase #{}: Volunteer cheated!".format(n+1))
        if switch == 1:
            f.write("\nCase #{}: {}".format(n+1, solution))
        if switch == 2:
            f.write("\nCase #{}: Bad magician!".format(n+1))
    else:
        if switch == 0:
            f.write("Case #{}: Volunteer cheated!".format(n+1))
        if switch == 1:
            f.write("Case #{}: {}".format(n+1, solution))
        if switch == 2:
            f.write("Case #{}: Bad magician!".format(n+1))
  
  
fo.close()
f.close()