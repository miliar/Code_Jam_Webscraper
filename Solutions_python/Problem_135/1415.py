__author__ = 'panmari'

import numpy as np

def make_alignment(f):
    alignment = ';'.join([f.readline(), f.readline(), f.readline(), f.readline()])
    return np.matrix(alignment)

answers = []
filename = 'A-small-attempt0.in'
with open(filename) as f:
    nr_problems = f.readline()
    while True:
        nextLine = f.readline()
        if nextLine == '':
            break
        first_answer = int(nextLine) - 1
        first_alignment = make_alignment(f)
        possible_cards = set(first_alignment[first_answer,:].flat)

        second_answer = int(f.readline()) - 1
        second_alignment = make_alignment(f)
        possible_cards2 = set(second_alignment[second_answer,:].flat)

        result = possible_cards.intersection(possible_cards2)
        if len(result) == 1:
            answers.append(result.pop())
        elif len(result) > 1:
            answers.append('Bad magician!')
        elif len(result) == 0:
            answers.append('Volunteer cheated!')

with open(filename + '.out', 'w') as f:
    for n, answer in enumerate(answers):
        f.write("Case #{}: {}\n".format(n + 1, answer))