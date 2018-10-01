"""
    Code Jam 2011 Qualification Round, Problem C

    gaz@bitplane.net

"""

with open('input.txt') as inputFile:
    testCount = int(inputFile.readline())
    
    for testNumber in range(testCount):

        # ignore, this isn't c!
        inputFile.readline()

        # read the numbers...
        allNumbers = [int(i) for i in inputFile.readline()[:-1].split(' ')]

        # if the numbers xor'd together are 0 then they're splittable
        if reduce(lambda x,y: x^y, allNumbers, 0) == 0:            
            # and the smallest number is the one we give him,
            # because that's how xor works
            # took me so bloody long to realise this that I'm embarassed
            result = str(sum(allNumbers) - min(allNumbers))
        else:
            result = "NO"
        
        # then we find the two smallest numbers that have opposing columns

        print("Case #{case}: {result}".format(case=testNumber+1, result=result))

