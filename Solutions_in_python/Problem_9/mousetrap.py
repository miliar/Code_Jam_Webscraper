"""
A very simple operation.

"""
import sys

class TestCase(object):

    def __init__(self, card_count, result_indices):
        self.card_count = card_count
        self.result_indices = result_indices

    def doTestCaseProcessing(self):
        """
        Ok, so how can we solve this without brute forcing it?

        Can we work in reverse? We know the last card will require:
        sum(range(1, 1+card_count))
        
        cards to be flipped before it is removed.

        The second to last card will require

        sum(range(1, card_count))

        cards to be flipped before it is removed.
        and so on, decrementing by one each time.

        If there are three cards, the decks, in reverse, look like this:
        [3]
        [3]
        [3]
        [3,2]
        [1,3,2]

        Four cards:
        [4]
        ...
        [3,4] The position of 3 is equal to 2 % 3 
        [3,4]
        [4,2,3]
        [1,4,2,3]

        Five:

        [5]

        [5,4]
        ...
        [5,4,3]
        [3,2,5,4]
        [1,3,2,5,4]

        Six:

        [6]
        ...
        [5,6]
        ...
        [4,5,6]
        ...
        [5,6,3,4]
        [4,2,5,6,3]
        [1,4,2,5,6,3]
        
        """
        result = ""
        output = []
        card_order = [self.card_count]

	for i in reversed(range(1, self.card_count)):
	    position = i % (len(card_order) + 1)
	    if position == 0:
		card_order.append(i)
	    elif position == 1:
		card_order = [i] + card_order
	    else:
		act_pos = position - 1
		card_order = card_order[-act_pos:] + [i] + card_order[:-act_pos]
        
        for index in self.result_indices:
            output.append(card_order[index - 1])

        result = " ".join(map(str, output))
        return result

def readTestCases(lines):
    test_cases = []
    test_case_count = int(lines[0])
    lines = lines[1:]
    while len(test_cases) < test_case_count:
        #What information is specific to this test case?
        card_count = int(lines[0])
        result_indices = map(int, lines[1].split(" "))[1:]
        test_cases.append(TestCase(card_count, result_indices))
        lines = lines[2:]
    return test_cases 
    

def processInputFile(filepath):
    data = open(filepath, "r").read()
    lines = data.split("\n")
    return readTestCases(lines)

if __name__ == "__main__":
    cases = processInputFile(sys.argv[1])
    case_count = 0
    for case in cases:
        case_count += 1
        print "Case #%d: %s" % (case_count, case.doTestCaseProcessing())
