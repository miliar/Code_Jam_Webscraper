import sys

input = sys.stdin
#input = open('A-small-attempt0.in')
T = int(input.readline().strip())

words = []
for i in xrange(T):
    words.append(input.readline().strip())

words2 = dict((w, True) for w in words)

def get_num(test_case):
    chars = set(test_case)
    positions = sorted((test_case.index(c), c) for c in chars)

    first_char = positions[0][1]
    trans_table = {}
    trans_table[first_char] = 1
    for i, c in enumerate(positions):
        if i == 1: continue
        if i == 0 and len(chars)>1:
            _pos, c = positions[1]
            trans_table[c] = 0
            continue
        elif i == 0 and len(chars) == 1:
            trans_table[c] = 1
            base = 2
            break
        pos, c = c
        trans_table[c] = i
    else:
        base = len(chars)

    res = 0
    for i, c in enumerate(test_case[::-1]):
        res += base**i * trans_table[c]

    return res

def process_case(case, i):
    #if i == 2: import pdb;pdb.set_trace()
    num = get_num(case)
    print "Case #%d: %d" % (i + 1, num)


for i, test_case in enumerate(words):
    process_case(test_case, i)


