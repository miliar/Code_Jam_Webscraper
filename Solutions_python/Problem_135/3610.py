def readMatrix():
    matrix=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    for i in range(4):
        tempLine = raw_input()
        tempLine=tempLine.split(" ")
        
        for j in range(4):
            matrix[i][j]=tempLine[j]
    return matrix

cases=int(raw_input())

for i in range(cases):
    case_str="Case #"+str(i+1)+": "

    line1=int(raw_input())
    matrix1 = readMatrix()
    
    line2=int(raw_input())
    matrix2 = readMatrix()
    
    intersection = set(matrix1[line1-1]).intersection(set(matrix2[line2-1]))
    if len(intersection) == 1:
        print case_str+str(intersection.pop())
    else:
        if len(intersection) > 1:
            print case_str+"Bad magician!"
        else:
            print case_str+"Volunteer cheated!"


