# Read the input
infile = open('B-small-attempt2.in.txt')
outfile = open('B-small-attempt2.out', 'w')
lines = infile.read().split('\n')
casecount = int(lines.pop(0))

# Solve the cases
def testCase(diners):
    return nextMinute(diners, 0, max(diners))

def nextMinute(diners, time, maxTime):
    #Increment time
    time+=1
    
    #Exit early if over maximum time
    if time>=maxTime:
        return maxTime
    
    #Special minute
    diners.sort()
    for i in range(len(diners)):
        #There must be at least 4 diners for a special minute to be worth it
        #Also ignore duplicate trees
        if diners[i]>=4 and (i==0 or diners[i]!=diners[i-1]):
            newdiners = diners[:]
            smallstack = newdiners[i]/2
            newdiners[i] -= smallstack
            newdiners.append(smallstack)
            num = nextMinute(newdiners, time, maxTime)
            if num<maxTime:
                maxTime = num
            if diners[i]==9:
                newdiners = diners[:]
                smallstack = newdiners[i]/3
                newdiners[i] -= smallstack
                newdiners.append(smallstack)
                num = nextMinute(newdiners, time, maxTime)
                if num<maxTime:
                    maxTime = num
                
    
    # Eat pancakes
    i=0
    while i < len(diners):
        diners[i] -= 1
        if diners[i]<=0:
            diners.pop(i)
        else:
            i+=1
    
    # Check if the plates are empty
    if len(diners)==0:
        return time
    
    # Otherwise, recurse to next minute
    num = nextMinute(diners, time, maxTime)
    if num<maxTime:
        maxTime = num
    
    #return the least minutes
    return maxTime


for casenum in range(1, casecount+1):
    d = lines.pop(0)
    nonemptydiners = map(int, lines.pop(0).split())
    print casenum, "-", nonemptydiners
    print >> outfile, "Case #%i: %i"%(casenum, testCase(nonemptydiners))