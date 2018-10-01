
def countHorizontal(lines, symbol):
    for line in lines:
        count = 0
        for char in line:
            if char == symbol or char == 'T':
                count += 1
        if count == 4:
            return True
    return False

def countVertical(lines, symbol):
    for i in range(4):
        count = 0
        for line in lines:
            if (line[i] == symbol or line[i] == 'T'):
                count += 1
        if count == 4:
            return True
    return False

def countDiagonal(lines, symbol):
    countLeft = 0
    countRight = 0
    left = [lines[0][0], lines[1][1], lines[2][2], lines[3][3]]
    right = [lines[0][3], lines[1][2], lines[2][1], lines[3][0]]

    for i in range(4):
        if left[i] == symbol or left[i] == 'T':
            countLeft += 1
        if right[i] == symbol or right[i] == 'T':
            countRight += 1
    return countRight == 4 or countLeft == 4

def solveFor(symbol, lines):
    if countHorizontal(lines, symbol) or countVertical(lines, symbol) or countDiagonal(lines, symbol):
        return True
    return False

def checkForEmpty(lines):
    for line in lines:
        for char in line:
            if char == '.':
                return True
    return False

def main():
    output = open('1.out', 'w')
    with open('A-large.in', 'r') as input:
        input.readline()
        lines = [0, 0, 0, 0]
        hasEmpty = False
        count = 0
        case = 0
        for line in input:
            line = line.split('\n')[0]
            if line == "":
                continue
            lines[count] = line
            if count == 3:
                case += 1
                hasEmpty = checkForEmpty(lines)
                statusX = solveFor('X', lines)
                statusO = solveFor('O', lines)
                
                finalStatus = ""
                if statusX:
                    finalStatus = 'X won'
                elif statusO:
                    finalStatus = 'O won'
                elif (not statusX) and (not statusO) and hasEmpty:
                    finalStatus = 'Game has not completed'
                elif (not statusX) and (not statusO) and (not hasEmpty):
                    finalStatus = 'Draw'
                    
                output.write('Case #{0}: {1}\n'.format(str(case), finalStatus))
            
            count = (count + 1) % 4
        output.close()

if __name__ == "__main__":
    main()
