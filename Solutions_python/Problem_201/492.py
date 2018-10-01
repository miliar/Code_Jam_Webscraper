def getCompletePowers(number):
    p = 0
    while 2 ** p - 1 <= number:
        p += 1
    return p - 1

def solve(stalls, people):
    cp = getCompletePowers(people)
    tcp = 2 ** cp
    num_people_left = people - (tcp - 1)
    numleft = stalls - (tcp - 1)
    gaps = numleft / (tcp)
    numextra = numleft % tcp
    size = gaps + 1 if num_people_left <= numextra else gaps
    if num_people_left != 0:
        if size % 2 == 0:
            return (size / 2, size / 2 - 1)
        else:
            return (size / 2, size / 2)
    else:
        cp = cp - 1
        tcp = 2 ** cp
        num_people_left = people - (tcp - 1)
        numleft = stalls - (tcp - 1)
        gaps = numleft / (tcp)
        numextra = numleft % tcp
        size = gaps + 1 if num_people_left <= numextra else gaps
        if size % 2 == 0:
            return (size / 2, size / 2 - 1)
        else:
            return (size / 2, size / 2)

numcases = input()
for test in xrange(1, numcases + 1):
    print 'Case #%d:' % test, ' '.join(map(str, solve(*map(int, raw_input().split()))))