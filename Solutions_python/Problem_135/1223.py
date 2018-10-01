__author__ = 'Javier'

def read_card_grid(lines, start_position):
    card_grid = []
    for j in range(4):
        card_grid.append(map(int,lines[start_position+j].split()))
    return card_grid

lines = tuple(open('A-small-attempt0.in', 'r'))

f = open('output.txt', 'w')

num_inputs = int(lines[0])

for i in range(num_inputs):
    first_answer = int(lines[1+10*i])
    first_grid = read_card_grid(lines, 2+10*i)
    second_answer = int(lines[6+10*i])
    second_grid = read_card_grid(lines, 7+10*i)

    cards = [card for card in first_grid[first_answer-1] if card in second_grid[second_answer-1]]

    if len(cards) == 1:
        print >> f, 'Case #%d: %d'%(i+1, cards.pop())
    elif len(cards) > 1:
        print >> f, 'Case #%d: Bad magician!'%(i+1)
    else:
        print >> f, 'Case #%d: Volunteer cheated!'%(i+1)



