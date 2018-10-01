from sys import stdin, stdout
from basics import *

def solve(N, P, people):
    people = map(lambda p:p%P, people)
    people_dict = dict((p, 0) for p in range(P))
    for p in set(people):
        people_dict[p] = people.count(p)

    happy = people_dict[0]
    people_dict[0] = 0

    if P == 4:
        combs = [{3:1, 1:1}, {2:2}, {3:2, 2:1}, {2:1, 1:2}, {3:4}, {1:4}]
    elif P == 3:
        combs = [{2:1, 1:1}, {2:3}, {1:3}]
    elif P == 2:
        combs = [{1:2}]
    
    added_comb = True
    while added_comb:
        added_comb = False
        for comb in combs:
            if all(people_dict[num] >= count for num, count in comb.items()):
                happy += 1
                for num, count in comb.items():
                    people_dict[num] -= count

                added_comb = True
                break

    if any(val > 0 for val in people_dict.values()):
        happy += 1

    return happy



T = int(stdin.readline())

for t in range(T):
    N, P = read_vals()
    people = read_vals()

    result = solve(N, P, people)

    stdout.write("Case #{}: {}\n".format(t+1, result))