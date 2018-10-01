import math

def isPalindrome(subject):
    valid = False

    if subject == subject[::-1]:
        valid = True

    return valid

def isSquare(subject):
    valid = False

    result = str(math.sqrt(int(subject)))

    pair = str(result).split(".")
    whole = pair[0]

    if int(whole) * int(whole) == int(subject):
        if isPalindrome(str(whole)):
            valid = True
    
    return valid

def countTargets(lower, upper):
    counter = 0

    for i in range(lower, upper + 1):
        if isPalindrome(str(i)) and isSquare(i):
            counter += 1
            
    return counter

def getFile():
    with open("C-small-attempt2.in", "r") as f:
        return f.read().split("\n")


def createOutput():
    content = getFile()
    with open("output.txt", "w") as f:
        for i in range(1, len(content)):
            val = content[i]
            if val != "":
                values = val.split(" ")
                lower = int(values[0])
                upper = int(values[1])
                count = countTargets(lower, upper)
                
                f.write("Case #" + str(i) + ": " + str(count) + "\n")

