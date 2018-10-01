import linecache
import shlex

#name of file with testing data
inputFile = 'A-small-attempt0.in'

#number of test cases
totalTestCases = int(linecache.getline(inputFile, 1))
arrRows = 4

for i in xrange(0, totalTestCases):
    firstPosition = int(linecache.getline(inputFile, 2+(2*(i*5))))
    secondPosition = int(linecache.getline(inputFile, 7+(2*(i*5))))
    firstCards = []
    secondCards = []
    for k in xrange(3+(2*(i*5)), (3+(2*(i*5)))+arrRows):
        firstCards.append(shlex.split(linecache.getline(inputFile, k)))
        secondCards.append(shlex.split(linecache.getline(inputFile, k+5)))

    if len(set(firstCards[firstPosition-1]).intersection(secondCards[secondPosition-1])) == 1:
        print "Case #%d: %d " % (i+1, int(list(set(firstCards[firstPosition-1]).intersection(secondCards[secondPosition-1]))[0]))
    elif len(set(firstCards[firstPosition-1]).intersection(secondCards[secondPosition-1])) == 0:
        print "Case #%d: %s " % (i+1, 'Volunteer cheated!')
    else:
        print "Case #%d: %s " % (i+1, 'Bad magician!')
