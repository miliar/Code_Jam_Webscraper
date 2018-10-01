def read_table(n, sep):
    table = []
    for i in range(n):
        row = map(int, raw_input().split(sep))
        table.append(row);
    return table

T = int(raw_input())

for j in range(T):
    g1 = int(raw_input())
    b1 = read_table(4, ' ')
    possible = b1[g1-1]
    g2 = int(raw_input())
    b2 = read_table(4, ' ')
    sol = [i for i in b2[g2-1] if i in possible]
    if not sol:
        result = "Volunteer cheated!"
    elif len(sol) > 1:
        result = "Bad magician!"
    else:
        result = sol[0]
    print "Case #{}: {}".format(j+1, result)