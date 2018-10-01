import sys

quaternions_map = {('1','1'):'1',
    ('1','i'):'i',
    ('1','j'):'j',
    ('1','k'):'k',
    ('i','1'):'i',
    ('i','i'):'-1',
    ('i','j'):'k',
    ('i','k'):'-j',
    ('j','1'):'j',
    ('j','i'):'-k',
    ('j','j'):'-1',
    ('j','k'):'i',
    ('k','1'):'k',
    ('k','i'):'j',
    ('k','j'):'-i',
    ('k','k'):'-1'}


def map_to_quaternions(x, y):
    s = quaternions_map[(x, y)]
    neg = 0
    if len(s) > 1:
        neg = 1
    return s[-1], neg

def check_if_ijk_front(inp):
    negative_counter = 0
    expected = ['i', 'j', 'k']
    dijk = ''
    curr = '1'

    while inp:
        next_ = inp[0]
        inp = inp[1:]
        curr, neg = map_to_quaternions(curr, next_)

        if (negative_counter==0 and neg):
            negative_counter = 1
        elif (negative_counter==1 and neg):
            negative_counter = 0

        if curr == expected[0] and curr != 'k':
            expected = expected[1:]
            dijk = dijk + curr
            curr = '1'

    dijk = dijk + curr

    if dijk == 'ijk' and (negative_counter==0):
        return True
    else:
        return False

if __name__=='__main__':
    count = 0
    for i in sys.stdin:
        if count == 0:
            count += 1
            continue

        if ' ' in i:
            _, mult = map(int, i.split())
            continue

        s = i.strip()

        print 'Case #%d:' % count, 'YES' if check_if_ijk_front(s*mult) else 'NO'
        count += 1
