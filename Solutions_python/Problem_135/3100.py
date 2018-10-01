T = int(raw_input())
for I in range(1, T+1):
    row = int(raw_input())
    for i in range(0, row-1):
        raw_input()
    cards = raw_input().split(' ')
    for i in range(row, 4):
        raw_input()

    col = int(raw_input())
    for i in range(0, col-1):
        raw_input()
    cards2 = raw_input().split(' ')
    for i in range(col, 4):
        raw_input()
    
    card = filter(lambda x: x in cards, cards2)
    if len(card) == 0:
        print("Case #%d: Volunteer cheated!" % I)
    elif len(card) == 1:
        print("Case #%d: %s" % (I, card[0]))
    else:
        print("Case #%d: Bad magician!" % I)