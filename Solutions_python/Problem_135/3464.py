file = open("A-small-attempt2.in", 'r')
input = file.readlines()
file.close()
file = open("A-small-attempt2.out", "w")

count = 1
N = int(input[0])

for k in range(1, N + 1):
    r1 = int (input[count])
    row1 = input[count + r1]
    count += 5
    r2 = int (input[count])
    row2 = input[count + r2]
    count += 5
    
    roww1 = []
    index = 0
    for i in range (len (row1)):
        if (row1 [i:i+1] == " "):
            roww1.append (row1 [index:i])
            index = i + 1
    roww1.append (row1 [index:-1])
    
    roww2 = []
    index = 0
    for i in range (len (row2)):
        if (row2 [i:i+1] == " "):
            roww2.append (row2 [index:i])
            index = i + 1
    roww2.append (row2 [index:-1])
    

    result = []
    for i in range (4):
        for j in range (4):
            if ( roww1 [i] == roww2 [j]):
                result.append (roww1 [i])
                roww1[i] = None
    
    print roww1, roww2, result
              
    if (len (result) == 1):
        file.write("Case #" + str(k) + ": " + str(result [0]) + "\n")
    elif (len (result) > 1):
        file.write("Case #" + str(k) + ": Bad magician!\n")
    else:
        file.write("Case #" + str(k) + ": Volunteer cheated!\n")
    
file.close()
