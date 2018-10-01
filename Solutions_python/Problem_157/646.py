def doCase(counts, line):
    length = int(counts[0])
    count = int(counts[1])
    line = line[0]
    strLen = length * count
    
    multiples = [[["1", False], ["i", False], ["j", False], ["k", False]], [["i", False], ["1", True], ["k", False], ["j", True]], [["j", False], ["k", True], ["1", True], ["i", False]], [["k", False], ["j", False], ["i", True], ["1", True]]]
    indices = ["1", "i", "j", "k"]
    
    negative = False
    finalString = line[0]
    
    nextCharIndex = 1
    
    while nextCharIndex < strLen:
        
        negativeString = ""
        if negative:
            negativeString = "-"
        print("Step #" + str(nextCharIndex) + ": " + negativeString + finalString)
        
        nextChar = line[nextCharIndex % length]
        
        if (len(finalString) == 1 and finalString[0] == 'i'):
            finalString = finalString + nextChar
        
        elif (len(finalString) == 2 and finalString[1] == 'j'):
            finalString = finalString + nextChar
            
        else:
            multiple = multiples[indices.index(finalString[len(finalString) - 1])][indices.index(nextChar)]
            
            finalStringList = list(finalString)
            finalStringList[len(finalString) - 1] = multiple[0]
            finalString = "".join(finalStringList)
            
            if (multiple[1] == True):
                negative = not negative
            
        nextCharIndex += 1
        
    negativeString = ""
    if negative:
        negativeString = "-"
    print("Step #" + str(nextCharIndex) + ": " + negativeString + finalString)
        
    if (len(finalString) == 3 and finalString[2] == 'k' and negative == False and nextCharIndex == strLen):
        return "YES"
    
    return "NO"

lines = [line.strip().split() for line in open('C-small-attempt1.in')]

out = open('output.txt', 'w')
for i in range(0, int(lines[0][0])):
    out.write("Case #" + str(i + 1) + ": " + str(doCase(lines[i * 2 + 1], lines[i * 2 + 2])) + "\n")
out.close
