'''
Created on 12 Apr 2014

@author: bluca
'''
import sys
from itertools import izip_longest, izip

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    num_cases = int(lines[0])
    lines = lines[1:]
    groups = izip_longest(*[iter(lines)]*10)
    for case, group in izip(range(1, num_cases+1), groups):
        row_1 = int(group[0])
        row_2 = int(group[5]) + 5
        set_1 = set(group[row_1].strip().split())
        set_2 = set(group[row_2].strip().split())
        card = set_1 & set_2
        if not card:
            answer = "Volunteer cheated!"
        elif len(card) > 1:
            answer = "Bad magician!"
        else:
            answer = card.pop()
        print "Case #%d: %s" % (case, answer)

if __name__ == '__main__':
    main()
