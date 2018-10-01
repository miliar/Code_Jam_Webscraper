inputFile = open("input", "r")
outputFile = open("output", "w")
n_test_cases = inputFile.readline()
for case in range(int(n_test_cases)):
    first_file = int(inputFile.readline()) - 1
    fGrid = []
    for i in range(4):
        fGrid.append(inputFile.readline()) 
    vect1 = fGrid[first_file][:-1].split(" ")
    second_file = int(inputFile.readline()) - 1
    for i in range(4):
        fGrid.append(inputFile.readline())     
    vect2 = fGrid[second_file + 4][:-1].split(" ")
    count = 0
    for i in vect1:
        if i in vect2:
            count = count + 1
            found = i
    if count == 0:
        outputFile.write("Case #" + str(case + 1) + ": Volunteer cheated!\n")
    elif count == 1:
        outputFile.write("Case #" + str(case + 1) + ": " + str(found) + "\n")
    elif count > 1:
        outputFile.write("Case #" + str(case + 1) + ": Bad magician!\n")

inputFile.close()
