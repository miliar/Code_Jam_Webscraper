#! /usr/bin/python3
import logging
log = logging.getLogger()
#log.setLevel(logging.DEBUG)

import argparse, csv

parser = argparse.ArgumentParser(description='Problem B - Magicka from Google Code Jam')
parser.add_argument('input', help='the input file given by the code jam website')
args = parser.parse_args()

with open(args.input, newline='') as f:
    reader = csv.reader(f, delimiter=' ')
    test_number = next(reader)[0]

    # for each test
    for i in range(int(test_number)):
        test = next(reader)

        combining = {}
        opposing = {}
        final = []
        # parse the test line

        for j in range(int(test[0])):
            combining[test[j+1][0]] = (test[j+1][1], test[j+1][2])
            combining[test[j+1][1]] = (test[j+1][0], test[j+1][2])
            logging.debug(combining)
        
        test = test[int(test[0])+1:]

        for j in range(int(test[0])):
            opposing[test[j+1][0]] = test[j+1][1]
            opposing[test[j+1][1]] = test[j+1][0]
            logging.debug(opposing)

        test = test[int(test[0])+1:]

        for j in range(0, int(test[0])):
            letter = test[1][j]

            logging.debug(final[-1:])
            logging.debug(letter)
            if not final:
                final = [letter]
            elif letter in combining and combining[letter][0] == final[-1:][0]:
                final = final[:-1]
                final.append(combining[letter][1])
            elif letter in opposing:
                if opposing[letter] in final:
                    final = []
                else:
                    final.append(letter)
            else:
                final.append(letter)

        print('Case #' + str(i+1) + ': [', end='')
        print(', '.join(final), end=']\n')
        logging.debug('\n')
