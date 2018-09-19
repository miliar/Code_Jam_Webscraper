def formatFile(filename, linesPerCase, removeNewline):
    testfile = open(filename, 'rU')
    contents = []
    formatted = []
    for line in testfile:
        if removeNewline:
            contents.append(line.replace('\n', ''))
        else:
            contents.append(line)
    numOfCases = int(contents.pop(0))
    for i in xrange(numOfCases):
        case = []
        for x in xrange(linesPerCase):
            case.append(contents.pop(0))
        formatted.append(case)
    return formatted

def createAnswer(answers, filename):
    answerfile = open(filename, 'w')
    for i in xrange(len(answers)):
        answerfile.write('Case #%d: %s\n' % (i+1, answers[i]))
