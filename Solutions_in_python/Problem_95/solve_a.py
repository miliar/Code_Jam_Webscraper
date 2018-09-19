#!/bin/python
import sys
import string

HINTS_PROBLEMS = [
    'y qee',
    'z',
    'ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv',
    ]
HINTS_ANSWERS = [
    'a zoo',
    'q',
    'our language is impossible to understand',
    'there are twenty six factorial possibilities',
    'so it is okay if you want to just give up',
]

# Check Converter
hints_problems_string = ''
for problem in HINTS_PROBLEMS:
    hints_problems_string += problem
hints_answer_string = ''
for answer in HINTS_ANSWERS:
    hints_answer_string += answer

if len(set(hints_problems_string)) == 27:
    print 'OK, I can translate'
else:
    print 'NG, I cannot translate'

trans = string.maketrans(hints_problems_string, hints_answer_string)

def main(file):
    outfile = file.replace('in', 'out')

    i_testcase = 0
    for line in open(file, 'r'):
        if i_testcase:
            result = line[:-1].translate(trans)
            print 'Case #%d: %s\n' % (i_testcase, result)
            # SAVE
            f = open(outfile, 'a')
            f.write('Case #%d: %s\n' % (i_testcase, result))
            f.close()
        i_testcase += 1

if __name__ == '__main__':
    main(sys.argv[1])
