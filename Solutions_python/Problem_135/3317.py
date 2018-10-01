inputFile = open('A-small-attempt0.in', 'r')
file1 = inputFile

file2 = open("MagicianTestAnswer.txt", 'w')
### test case iteration ###

def magicFunction (file1):
    firstAnswer = int(file1.readline())
    
    list1 = []
    for n1 in range(4):
        list1.append(file1.readline())

    secondAnswer = int(file1.readline())
    list2 = []
    for n2 in range(4):
        list2.append(file1.readline())

    
    magicAnswer = []
    
    word1 = list1[firstAnswer-1]
    word1 = word1[:word1.index("\n")]

    word2 = list2[secondAnswer-1]
    word2 = word2[:word2.index("\n")]
    
    
    
    wordList1 = word1.split(' ')
    wordList2 = word2.split(' ')

    
    for letter1 in wordList1:
        for letter2 in wordList2:
            if letter1 == letter2:
                magicAnswer.append(letter1)

    if len(magicAnswer) == 1:
        return magicAnswer[0]
    elif len(magicAnswer) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


### Given their input, Iterate test case things ###

caseNumber = int(file1.readline())

for caseN in range(caseNumber):
    N = caseN + 1
    file2.write("Case #"+str(N)+ '' +  ":" + ' ' + magicFunction(file1) + '\n')

file2.close()
