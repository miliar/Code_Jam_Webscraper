#!/usr/bin/env python3

T = int(input())
for i in range(T):
    answer1 = int(input())
    cards1 = []
    for j in range(4):
        cards1.append([int(x) for x in input().split()])
    answer2 = int(input())
    cards2 = []
    for j in range(4):
        cards2.append([int(x) for x in input().split()])

    possible_cards = []
    for j in cards2[answer2-1]:
        if j in cards1[answer1-1]:
            possible_cards.append(j)

    if len(possible_cards) == 0:
        print('Case #{0}: {1}'.format(i+1, 'Volunteer cheated!'))
    elif len(possible_cards) == 1:
        print('Case #{0}: {1}'.format(i+1, possible_cards[0]))
    else:
        print('Case #{0}: {1}'.format(i+1, 'Bad magician!'))
