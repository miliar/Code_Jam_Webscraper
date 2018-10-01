from codecs import open as cOpen
from sys import argv

def takeFive(f):
    """Parses the next 5 lines, returns possible numbers
        Args:   f; file
        Returns: List of int
    """
    rowguess = int(f.next().strip())
    for i in xrange(4):
        row = [int(e) for e in f.next().strip().split(' ')]
        if i+1 == rowguess:
            # must be picked given limits. This is unsafe if 1<=answer<=4 constraint doesn't hold
            chosenrow = row
    return chosenrow
            
def deduceTrick(row1, row2):
    leftovers = filter(lambda x: x in row1, row2)
    # 1 left, we have th match
    if len(leftovers) == 1:
        return leftovers[0]
    # more than one left, the magician screwed up
    elif len(leftovers) > 1:
        return 'Bad magician!'
    # none left, we've a liar
    else:
        return 'Volunteer cheated!'

def main(path):
    results = []
    with cOpen(path, encoding='utf-8-sig') as input:
        testCases = int(input.next().strip())
        for i in range(1,testCases + 1):
            rowOne = takeFive(input)
            rowTwo = takeFive(input)
            result = deduceTrick(rowOne, rowTwo)
            results.append('Case #%s: %s' % (i, result))
    return results
        
if __name__ == '__main__':
    # tester = main('testinput.txt')
    # assert tester[0] == '7'
    # assert tester[1] == 'Case #2: Bad magician!'
    # assert tester[2] == 'Case #3: Volunteer cheated!'
    if len(argv) > 1:
        for line in main(argv[1]):
            print line