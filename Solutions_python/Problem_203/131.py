import string

def solve(cake):
    for row in cake:
        initials = filter(lambda c: c is not '?', row)
        if len(initials) == 0:
            continue
        initial = initials[0]
        for i in range(len(row)):
            if row[i] == '?':
                row[i] = initial
            else:
                initial = row[i]

    filled_in_rows = filter(lambda row: row[0] is not '?', cake)
    row = filled_in_rows[0]
    for i in range(len(cake)):
        if cake[i][0] == '?':
            for j in range(len(cake[0])):
                cake[i][j] = row[j]
        else:
            row = cake[i]
    return to_string(cake)

def to_string(cake):
    return '\n' + string.join([string.join(row, '') for row in cake], '\n')    

def parse():
    R, C = [int(i) for i in raw_input().split()]
    cake = []
    for r in range(R):
        row = [c for c in raw_input()]
        cake.append(row)
    return cake

T = int(raw_input())
for t in range(1, T+1):
    cake = parse()
    print("Case #{0}: {1}".format(t, solve(cake)))