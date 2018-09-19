
def runCase(data, n):
    if data[1] == 4:
        if data[0] == 1:
            if x in (1,2):
                return "GABRIEL"
            else:
                return "RICHARD"
        elif data[0] == 2:
            if x in (1,2):
                return "GABRIEL"
            else:
                return "RICHARD"
        elif data[0] == 3:
                return "GABRIEL"
        elif data[0] == 4:
            if x in (1,2,4):
                return "GABRIEL"
            else:
                return "RICHARD"
    if data[1] == 3:
        if data[0] == 1:
            if x == 1:
                return "GABRIEL"
            else:
                return "RICHARD"
        elif data[0] == 2:
            if x == 4:
                return "RICHARD"
            else:
                return "GABRIEL"
        elif data[0] == 3:
            if x in (2,4):
                return "RICHARD"
            else:
                return "GABRIEL"
            
    if data[1] == 2:
        if data[0] in (1,2):
            if x in (4,3):
                return "RICHARD"
            else:
                return "GABRIEL"

    elif data[1] == 1:
        if data[0] == 1:
            if x == 1:
                return "GABRIEL"
            else:
                return "RICHARD"

 

f = open('D-small-attempt.in', 'r')
output = ""

amountCases = int(f.readline())

for caseNumber in range(amountCases):
    print(caseNumber)
    data = [int (i) for i in f.readline().split()]
    x = data.pop(0)
    data.sort()
    
    result = runCase(data, x)
    output += "Case #" + str(caseNumber+1) + ": " + str(result) + "\n"

        
print(output)

