
import sys
import math



################################################################################


def isPalindrome(number):

    elements = len(number)
    for index in range(0, elements / 2):
        if (number[index] != number[elements - 1 - index]):
            return False
    
    return True


def squareRoot(number):
    
    root = int(math.sqrt(number))
    
    if (root * root) == number:
        return root
    
    return 0
    
    
def isFairAndSquare(number):

    if not isPalindrome(str(number)):
        return False
        
    root = squareRoot(number)
    if (0 == root):
        return False
        
    return isPalindrome(str(root))
    
    
def countFairAndSquare(start, end):

    counter = 0
    
    for index in range(start, end + 1):
        if isFairAndSquare(index):
            counter += 1
    
    return str(counter)
    
    
################################################################################



def processFile(inputFile, outputFile):

    input = open(inputFile, 'r')
    output = open(outputFile, 'w')
    
    caseNumber = 1
    limit = 0
    counter = 0
    
    
    for line in input:
        line = line.rstrip('\r\n')
        
        if (0 == limit):
            limit = int(line)
        else:
            entries = line.split(' ')
            count = countFairAndSquare(int(entries[0]), int(entries[1]))
            output.write("Case #" + str(caseNumber) + ": " + count + "\n")
            
            caseNumber += 1
            
            counter += 1
            if counter >= limit:
                break
        
    output.close()
    input.close()


def main(argv):
    
    processFile(argv[0], argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])