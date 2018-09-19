"""
Kamal Wood
Google Code Jam 2009
The Next Number
Saturday, 12 September 2009
"""

def next(line, digits):
    temp = digits[:]

    loc = 0
    while loc < len(line):
        if line[loc] != '0':
            temp[int(line[loc])] -= 1
        loc += 1

    if temp == [None,0,0,0,0,0,0,0,0,0]:
        return True

    return False

def main():
    outFile = open("B-small-attempt3.out","w")
    with open("B-small-attempt3.in","r") as inFile:
        total = int(inFile.readline())
        N = 1

        while N <= total:
            line = inFile.readline()
            if line[-1] == '\n':
                line = line[:-1]
            number = int(line)

            digits = [None,0,0,0,0,0,0,0,0,0]
            for char in line:
                if char != '0':
                    digits[int(char)] += 1

            number += 1
            line = str(number)

            while not next(line, digits):
                number += 1
                line = str(number)

            outFile.write("Case #%d: %d\n" %(N, number))

            N += 1

    outFile.close()

main()