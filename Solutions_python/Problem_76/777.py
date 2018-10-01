import functools

def choosePile(vals):
    exorVals = functools.reduce(lambda x,y: x^y, vals)
    if (exorVals != 0 or len(vals)<2):
        #not possible if odd number of 1s in any column
        return 'NO'
    #otherwise give back a candy
    minVal = min(vals)
    sumVals = sum(vals)
    #print (vals)
    #print ("min:", minVal, "  max:", sumVals)
    return sumVals - minVal

def strToVals(strIn):
    vals = strIn.split()
    vals = [int(i) for i in vals]
    return vals

def solve(inF, outF):
    """usage: solve('in.txt', 'out.txt')"""
    fIn = open(inF, 'r')
    fOut = open(outF, 'w')
    
    cases = int(fIn.readline())
    for case in range (1, cases+1):
        fIn.readline() #remove line telling us the number of candies
        vals = strToVals(fIn.readline())
        choice = choosePile(vals)
        soln = "Case #" + str(case) + ": " + str(choice)
        print (soln)
        fOut.write(soln + '\n')

    fIn.close()
    fOut.close()

        
  
    
