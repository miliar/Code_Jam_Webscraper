T = input()
for t in range(1, T + 1):
    both_answers = input()
    cards = []
    for i in range(4):
        cards.append(map(int, raw_input().split()))
    s1 = set(cards[both_answers - 1])
    both_answers = input()
    cards = []
    for i in range(4):
        cards.append(map(int, raw_input().split()))
    s2 = set(cards[both_answers - 1])
    ret = s1 & s2
    if len(ret) == 1:
        print "Case #%d: %d" % (t, ret.pop())
    elif len(ret) == 0:
        print "Case #%d: Volunteer cheated!" % t
    else:
        print "Case #%d: Bad magician!" % t
