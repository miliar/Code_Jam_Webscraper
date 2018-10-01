import sys

in_file = sys.argv[1]
out_file = in_file[:-2] + 'out'

with open(in_file) as f:
    T = int(f.readline())
    for t in range(T):
        a1 = int(f.readline()) - 1
        cards1 = []
        for i in range(4):
            cards1.append([int(card) for card in f.readline().strip().split()])
        a2 = int(f.readline()) - 1
        cards2 = []
        for i in range(4):
            cards2.append([int(card) for card in f.readline().strip().split()])

        card = set(cards1[a1]) & set(cards2[a2])
        if len(card) == 1:
            res = str(card.pop())
        elif len(card) > 1:
            res = 'Bad magician!'
        else:
            res = 'Volunteer cheated!'

        print 'Case #%s: %s' % (t+1, res)



