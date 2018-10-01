#main.py

from Finder import *

#INPUT_FILE  = "input.txt"
#OUTPUT_FILE = "output.txt"

#INPUT_FILE  = "A-small-attempt0.in"
#OUTPUT_FILE = "A-small-attempt0.out"

INPUT_FILE  = "A-large.in"
OUTPUT_FILE = "A-large.out"

if __name__=="__main__":

    inputFile = file(INPUT_FILE)
    outputFile = file(OUTPUT_FILE, "w")
    
    numTestCases = int(inputFile.readline())

    for tcIndex in range(numTestCases):
    
        numNumbers = int(inputFile.readline())
        print "numbers:", numNumbers
   
        x = inputFile.readline().rstrip().split()
        y = inputFile.readline().rstrip().split()

        x = [long(value) for value in x]
        y = [long(value) for value in y]
        print "x:", x
        print "y:", y

        finder = Finder(x,y)

        minScalar = finder.getMinScalar()

        outputFile.write("Case #"+str(tcIndex+1)+": ")
        outputFile.write('%d ' % minScalar)
        outputFile.write("\n")

    outputFile.close()
    inputFile.close()
    

            
            
