def read_words(afile):
    words = []
    for line in afile:
            words.append(line.strip())
    return words

def mult(a, b):
    if (a == 1):
        return b
    if (a == 2):
        if (b == 1):
            return 2
        if (b == 2):
            return -1
        if (b == 3):
            return 4
        if (b == 4):
            return -3
    if (a == 3):
        if (b == 1):
            return 3
        if (b == 2):
            return -4
        if (b == 3):
            return -1
        if (b == 4):
            return 2
    
    if (a == 4):
        if (b == 1):
            return 4
        if (b == 2):
            return 3
        if (b == 3):
            return -2
        if (b == 4):
            return -1
    
    if (a == -1):
        return -b
    if (a == -2):
        if (b == 1):
            return -2
        if (b == 2):
            return 1
        if (b == 3):
            return -4
        if (b == 4):
            return 3
    if (a == -3):
        if (b == 1):
            return -3
        if (b == 2):
            return 4
        if (b == 3):
            return 1
        if (b == 4):
            return -2
    if (a == -4):
        if (b == 1):
            return -4
        if (b == 2):
            return -3
        if (b == 3):
            return 2
        if (b == 4):
            return 1



def evalString(string, char): # make sure to pass in the number for char

    result = 1
    done = False
    for i in range(len(string)):
        
        if(string[i] == 'i'):
            num = 2
        if(string[i] == 'j'):
            num = 3
        if(string[i] == 'k'):
            num = 4

        result = mult(result, num)

        if (result == char):
            return i
            done = True
    if (done == False):
        return -1


filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text

for i in range(int(T)):
    firstLine = aList[2*i]
    L = int(firstLine.split()[0])
    X = int(firstLine.split()[1])
    
    secondLine = aList[2*i + 1]

    string = secondLine*X
    
    hasI = False
    hasJ = False
    hasK = False
    isPossible = False

    if (len(string) > 0):
        FinishedI = evalString(string, 2)
        if (FinishedI > -1):
            string = string[FinishedI+1:]

            if (len(string) > 0):
                FinishedJ = evalString(string, 3)
                if (FinishedJ > -1):
                    string = string[FinishedJ+1:]

                    if (len(string) > 0):
                        FinishedK = evalString(string, 4)
                        if (FinishedK > -1):
                            if (len(string) == FinishedK+1):
                                isPossible = True
                                print ("Case #"+str(i+1)+": YES")
                            else:
                                string = string[FinishedK+1:] #non-empty
                                while (len(string) > 0):

                                    derp = evalString(string, 1)
                                    
                                    if (derp > -1):
                                        if (len(string) == derp+1):
                                            isPossible = True
                                            print ("Case #"+str(i+1)+": YES")
                                            
                                        string = string[derp+1:]
                                        
                                    else:
                                        break

    
    if (isPossible == False):
        print ("Case #"+str(i+1)+": NO")

