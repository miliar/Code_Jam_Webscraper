def getCount(smax, s):
    added = 0
    clapped = 0
    for shyness, people in enumerate(s):
        people = int(people)
        if not people:
            continue
        if clapped < shyness:
            added += shyness - clapped
            clapped += shyness - clapped
        clapped += people
    return added

def test():
    assert getCount(4, '11111') == 0
    assert getCount(1, '09') == 1
    assert getCount(5, '110011') == 2
    assert getCount(0, '1') == 0
    assert getCount(6, '0100001') == 5
    assert getCount(6, '2200101') == 1

if __name__ == '__main__':
    import trace
    test()
    import sys
    with sys.stdin as f:
        T = int(f.readline())
        i = 1
        for line in f:
            sm, s = line.split()
            print "Case #%d: %d" % (i, getCount(int(sm), s))
            i += 1
