def solve():
    row = int(raw_input()) - 1
    rows = []
    for i in range(4):
        rows.append(map(int, raw_input().split(" ")))

    set1 = set(rows[row])

    row = int(raw_input()) - 1
    rows = []
    for i in range(4):
        rows.append(map(int, raw_input().split(" ")))

    set2 = set(rows[row])

    answer = set1.intersection(set2)

    if len(answer) == 1:
        return str(next(iter(answer)))
    elif len(answer) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

cases = int(raw_input())

for case in range(cases):
    answer = solve()
    print "Case #{}: {}".format(case + 1, answer)