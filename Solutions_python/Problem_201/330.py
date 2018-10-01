import math as math
file = open("C-large.in", "r")
infile = [i.split() for i in file.readlines()]
test_cases = int(infile[0][0])
input_cases = []
newfile = open("GCI_3.txt", "w")
for j in range(1, test_cases + 1):          #first element is number of test cases (just checking that)
    input_cases.append(infile[j])
for j in range(len(input_cases)):
    stalls = int(input_cases[j][0])
    people = int(input_cases[j][1])
    layers = 1
    inserted = 0
    while people > layers:            #give layer just before we have to end
        inserted += layers
        people -= layers
        layers = layers * 2
    stalls -= inserted
    inserted += 1                   #insert 1 for the     
    large_stalls = stalls % inserted
    stalls = stalls // inserted         #finds smallest stall
    if people <= large_stalls:           #checking if they pass a threshold for those stall spaces that are smaller
         stalls += 1
    stalls -= 1
    minimum = stalls // 2
    maximum = (stalls + 1) //  2
    print("Case #{0}: {1} {2}".format(j + 1, maximum, minimum))
    newfile.write("Case #{0}: {1} {2}\n".format(j + 1, maximum, minimum))
newfile.close()
