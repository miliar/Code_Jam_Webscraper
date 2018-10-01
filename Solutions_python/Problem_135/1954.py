
T = int(raw_input())
for case in range(1, T+1):
    r1 = int(raw_input())
    cards1 = [raw_input() for _ in range(4)][r1-1]
    r2 = int(raw_input())
    cards2 = [raw_input() for _ in range(4)][r2-1]
    result = set(cards1.split()) & set(cards2.split())
    if len(result) == 1:
        print "Case #%d: %s" % (case, result.pop())
    elif len(result) == 0:
        print "Case #%d: Volunteer cheated!" % case
    else:
        print "Case #%d: Bad magician!" % case

