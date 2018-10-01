maxShy = []
numPeople = []

fin = open("A-small-attempt1.in", "r")
temp = True
for line in fin:
    if temp:
        Cases = int(line)
        temp = False
    else:
        num = line.strip()
        maxShy.append(int(num[0]))
        numPeople.append(num[2:])
fin.close()

fout = open("StandinOvation.txt", 'w')
for case in range(Cases):
    friends = 0
    singleNums = list(numPeople[case])
    sumPpl = 0
    for j in range(maxShy[case] + 1):
        if int(singleNums[j]) > 0:
            if sumPpl < j:
                while sumPpl != j:
                    friends += 1
                    sumPpl += 1
        sumPpl += int(singleNums[j])
    print("Case #" + str(case+1) + ": " + str(friends), file=fout)
fout.close()




