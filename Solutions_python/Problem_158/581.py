# if unomino then GABRIEL
# if omino >= 7 then RICHARD
# if domino and R * C not even then RICHARD
# if domino and R * C even then GABRIEL
# In general, if omino size does not divide R * C, then RICHARD

def detWinner(X, R, C):
    if X == 1:
        return "GABRIEL"

    elif X >= 7: # each X-Omino X>7 has hole in it, no way to fill w/o overlap
        return "RICHARD"

    elif R * C % X != 0:
        return "RICHARD"

    elif X == 2:
        return "GABRIEL"

    elif R <= X // 2 or C <= X // 2:
        return "RICHARD"

    else:
        return "GABRIEL"

inp = """64
2 2 2
2 1 3
4 4 1
3 2 3
4 2 3
3 1 4
2 1 4
1 3 2
3 4 4
1 1 4
4 1 2
2 3 2
1 2 1
1 3 1
3 2 2
4 4 3
3 1 1
1 2 4
1 1 3
4 4 2
3 4 2
2 4 2
3 3 2
4 2 1
2 1 1
2 4 3
4 4 4
1 2 2
2 4 1
4 3 4
2 4 4
3 1 2
2 2 3
4 2 4
1 4 2
3 2 1
1 3 3
2 2 4
1 4 3
2 1 2
1 1 2
3 4 1
3 3 1
2 3 3
1 2 3
2 2 1
3 3 4
3 2 4
4 1 4
4 3 3
2 3 4
4 1 1
3 4 3
1 4 4
4 1 3
4 3 1
4 2 2
3 3 3
1 3 4
2 3 1
3 1 3
1 4 1
4 3 2
1 1 1""".split('\n')

T = int(inp[0])
inp = inp[1:]

for q in range(T):
    case = inp[q]
    X = int(case.split(' ')[0])
    R = int(case.split(' ')[1])
    C = int(case.split(' ')[2])
    print("Case #%d: %s" % ((q+1), detWinner(X, R, C)))






























