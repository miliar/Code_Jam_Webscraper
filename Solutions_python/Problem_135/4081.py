datain = open('A-small-attempt3.in', 'r')
dataout = open('result.txt', 'w')

for length in range(int(datain.readline())):

    choice = int(datain.readline())
    row1 = datain.readline()
    row2 = datain.readline()
    row3 = datain.readline()
    row4 = datain.readline()
    res1 = []
    res2 = []

    if(choice == 1):
        res1 = row1.split()
    elif(choice == 2):
        res1 = row2.split()

    elif(choice == 3):
        res1 = row3.split()

    elif(choice == 4):
        res1 = row4.split()

    choice2=int(datain.readline())
    row21 = datain.readline()
    row22 = datain.readline()
    row23 = datain.readline()
    row24 = datain.readline()

    if(choice2 == 1):
        res2 = row21.split()

    elif(choice2 == 2):
        res2 = row22.split()

    elif(choice2 == 3):
        res2 = row23.split()

    elif(choice2 == 4):
        res2 = row24.split()

    list1 = []
    for l1 in res1:
        for l2 in res2:
            if l2 == l1:
                list1.append(l1)

    if(len(list1) == 1):
        dataout.write('Case #' + str(length+1) + ': ' + list1[0] + '\n')

    elif(len(list1) > 1):
        dataout.write("Case #"+str(length+1)+": Bad magician!"+ '\n')

    elif(len(list1) < 1):
        dataout.write("Case #"+str(length+1)+": Volunteer cheated!"+ '\n')

datain.close()
dataout.close()
