import sys
import re


def checkrow(cells, c):
    for i in range(4):
        if c*4 in cells[i]:
            return True
        if c*3 in cells[i] and 'T' in cells[i]:
            return True
    return False


def checkdiag(rows, c):
    num = 0
    hast = False
    for i in range(4):
        if (rows[i])[i] == c:
            num += 1
        if (rows[i])[i] == 'T':
            hast = True
    if num == 4:
        return True
    if num == 3:
        return hast
    
    num = 0
    hast = False
    for i in range(4):
        if (rows[i])[3-i] == c:
            num += 1
        if (rows[i])[3-i] == 'T':
            hast = True
    if num == 4:
        return True
    if num == 3:
        return hast

    
def checkgameover(rows):
    for i in range(4):
        if '.' in rows[i]:
            return False
    return True


def main():
    f = open('A-small-attempt0.in', 'r')
    output = open('A-small-attempt0.out', 'w')
    text = f.read()
    f.close()
    lines = re.split("[\n|\r]",text)
    T = int(lines[0])
    
    for n in range(T):
        rows = []
        for x in range(4):
            rows.append(lines[n*5+1+x])

        cols = []
        for x in range(4):
            cols.append((lines[n*5+1])[x]+(lines[n*5+2])[x]+(lines[n*5+3])[x]+(lines[n*5+4])[x])

        if checkrow(rows, 'X') or checkrow(cols, 'X') or checkdiag(rows, 'X'):
            output.write('Case #' + str(n+1) + ': X won' +'\n')
        elif checkrow(rows, 'O') or checkrow(cols, 'O') or checkdiag(rows, 'O'):
            output.write('Case #' + str(n+1) + ': O won' +'\n')
        elif checkgameover(rows):
            output.write('Case #' + str(n+1) + ': Draw' +'\n')
        else:
            output.write('Case #' + str(n+1) + ': Game has not completed' +'\n')
            
    output.close()

    

if __name__ == '__main__':
    main()
