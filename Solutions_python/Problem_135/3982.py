#!/usr/bin/env python
OUTPUT_1 = 0
OUTPUT_2 = 'Bad magician!'
OUTPUT_3 = 'Volunteer cheated!'


def main():
    i = open('round1input')
    num_test_cases = int(i .readline())
    card_array_round1, card_array_round2 = [], []
    result = ''
    for test_case in xrange(num_test_cases):
        for loop in xrange(2):
            row_choice = int(i.readline())
            for line in xrange(4):
                cards = i.readline()
                if line + 1 is row_choice:
                    if loop is 0:
                        card_array_round1 = [int(x) for x in cards.split(' ')]
                    else:
                        card_array_round2 = [int(x) for x in cards.split(' ')]
                        card_found, result = False, False
                        for x in card_array_round1:
                            if x in card_array_round2:
                                if card_found:
                                    result = OUTPUT_2
                                else:
                                    card_found = True
                                    result = x
                        if not result:
                            result = OUTPUT_3
        print "Case #" + str(test_case + 1) + ": " + str(result)



if __name__=='__main__':
    main()