def getMinimumTimeRequired(C, F, X):
    rate = 2
    numberOfSecondsTaken = 0.00
    while( True ):
        if ((X / rate) < ((C / rate ) + (X / (rate + F)))):
            numberOfSecondsTaken = numberOfSecondsTaken + (X/rate)
            break
        else:
            numberOfSecondsTaken = numberOfSecondsTaken + (C/rate)
            #print numberOfSecondsTaken
            rate = rate + F
    return numberOfSecondsTaken

def run():
    f = open("cookieClickerInput2.txt")
    numberOfTestCases = int(f.readline())
    for i in range(numberOfTestCases):
        line = f.readline()
        C = float(line.split()[0])
        F = float(line.split()[1])
        X = float(line.split()[2])
        
        print "Case #" + str(i + 1) + ": " + str(getMinimumTimeRequired(C,F,X))

#print getMinimumTimeRequired(500.0, 4.0, 2000.0 )

run()
