# Qualification Round 2012
# B. Dancing With the Googlers
# Roman Stolper (romocop)

# imports
import sys;
import string;

def main():
    # get input filename from command line args
    if (len(sys.argv) != 2):
        print "Must specify input file!";
        return 1;

    inputFile = str(sys.argv[1]);
    outputFile = inputFile + ".out";
        
    # open input file
    f_in = open(inputFile, 'r');
    f_out = open(outputFile, 'w');
    
    runTests(f_in, f_out);

    f_in.close();
    f_out.close();

def runTests(f_in, f_out):
    numTests = int(f_in.readline());
    for i in range(0, numTests):
        runTest(f_in, f_out, i+1);

def runTest(f_in, f_out, testNum):
    line = f_in.readline();
    (n, s, p, pointTotals) = parseLine(line);
    maxGooglers = analyzeScores(n, s, p, pointTotals);
    #print "Line: " + line + "Result: " + str(maxGooglers);
    f_out.write("Case #" + str(testNum) + ": " + str(maxGooglers) + "\n");
    
def parseLine(line):
    pieces = string.split(line);
    offset = 0;
    n = int(pieces[offset]); offset +=1;
    s = int(pieces[offset]); offset +=1;
    p = int(pieces[offset]); offset +=1;
    pointTotals = list();
    for i in range(0, n):
        pointTotal = int(pieces[offset]); offset +=1;
        pointTotals.append(pointTotal);
        
    return (n, s, p, pointTotals);
    
def analyzeScores(n, s, p, pointTotals):
    maxGooglers = 0;
    numSurprisesRemaining = s;
    minScoreWithoutSurprise = (p + max(p-1,0) + max(p-1,0));
    minScoreWithSurprise = (p + max(p-2,0) + max(p-2,0));
    for pointTotal in pointTotals:
        if (pointTotal >= minScoreWithoutSurprise):
            maxGooglers += 1;
        elif (pointTotal >= minScoreWithSurprise and numSurprisesRemaining > 0):
            maxGooglers += 1;
            numSurprisesRemaining -= 1;
    return maxGooglers;

main();