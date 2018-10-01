import sys

sys.stdin = open('A-small-attempt0.in')
sys.stdout = open('out1.txt', 'w')


N = int(input())

for case in range(N):
    cards1 = []
    cards2 = []
    row1 = int(input())
    for _ in range(4):
        cards1.append([int(x) for x in input().split()])
    row2 = int(input())
    for _ in range(4):
        cards2.append([int(x) for x in input().split()])
    intersect = []
    for card in cards1[row1-1]:
        if card in cards2[row2-1]:
            intersect.append(card)
    message = "Bad magician!"
    if len(intersect) == 1:
        message = str(intersect[0])
    elif len(intersect) == 0:
        message = "Volunteer cheated!"
    print("Case #%d: %s" % (case+1, message))
sys.stdout.close()
