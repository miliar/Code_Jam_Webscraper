

f = open('test.txt', 'r')
r = open('result.txt', 'w')

tests = int(f.readline())

for t in range(tests):
    a1 = int(f.readline())
    
    for i in range(4):
        line = f.readline()
        if i == a1 - 1:
            cards1 = [int(card) for card in line.split()]

    a2 = int(f.readline())

    for i in range(4):
        line = f.readline()
        if i == a2 - 1:
            cards2 = [int(card) for card in line.split()]
    
    count = 0
    for card in cards1:
        if card in cards2:
            realCard = card
            count += 1
    
    if count == 0:
        r.write('Case #{0}: {1}\n'.format(t + 1, 'Volunteer cheated!'))
    elif count == 1:
        r.write('Case #{0}: {1}\n'.format(t + 1, realCard))
    elif count > 1:
        r.write('Case #{0}: {1}\n'.format(t + 1, 'Bad magician!'))
    