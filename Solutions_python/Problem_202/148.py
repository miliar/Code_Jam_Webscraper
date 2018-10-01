def get_score(bd, N):
    score = 0
    for i in xrange(N):
        for j in xrange(N):
            if bd[i][j] == 'o':
                score += 2
            elif bd[i][j] == 'x':
                score += 1
            elif bd[i][j] == '+':
                score += 1

    # print "score: %d" % score
    return score

def check_row(x, y, bd, N):
    total = 0
    plus_count = 0
    for j in xrange(y+1):
        val = bd[x][j]
        if val != '.':
            total += 1
            if val == '+':
                plus_count += 1

    return plus_count+1 >= total

def check_col(x, y, bd, N):
    total = 0
    plus_count = 0
    for i in xrange(x+1):
        val = bd[i][y]
        if val != '.':
            total += 1
            if val == '+':
                plus_count += 1

    return plus_count+1 >= total

def check_diag(x, y, bd, N):
    total = 0
    xx_count = 0
    for i in xrange(x+1):
        j = i+x-y
        if j >= 0 and j < N:
            val = bd[i][j]
            if val != '.':
                total += 1
                if val == 'x':
                    xx_count += 1

    return xx_count+1 >= total

def check_diag_back(x, y, bd, N):
    total = 0
    xx_count = 0
    for i in xrange(x+1):
        j = x+y-i
        # print i, j
        if j >= 0 and j < N:
            val = bd[i][j]
            if val != '.':
                total += 1
                if val == 'x':
                    xx_count += 1

    return xx_count+1 >= total

def check(x, y, bd, N):
    return check_row(x, y, bd, N) \
        and check_col(x, y, bd, N) \
        and check_diag(x, y, bd, N) \
        and check_diag_back(x, y, bd, N)

def rec(i, j, bd, N, models):
    # print i, j
    # print bd
    if j == N:
        return rec(i+1, 0, bd, N, models)

    if i == N:
        score = get_score(bd, N)
        # print bd
        # print "^^^score: %d" % score
        # print score, models
        return score, models

    max_score = 0
    max_models = []
    for m in ['o', 'x', '+', '.']:
        # print "bd[%d][%d] = %s, m = %s" % (i, j, bd[i][j], m)

        if (bd[i][j] == '.' and m in ['o', 'x', '+']) \
            or (bd[i][j] in ['+', 'x'] and m == 'o') \
            or (bd[i][j] == m):
                orig_model = bd[i][j]
                bd[i][j] = m
                valid = check(i, j, bd, N)
                # print "set (%d, %d) to %s => valid: %s" % (i, j, m, valid)
                if valid:
                    models_copy = models[:]
                    if m != orig_model:
                        models_copy.append((m, i+1, j+1))

                    # print 'Before: ', models_copy

                    score, models_copy = rec(i, j+1, bd, N, models_copy)

                    # print 'After: ', models_copy

                    if score > max_score:
                        max_score = score
                        max_models = models_copy

                bd[i][j] = orig_model

    return max_score, max_models

def solve():
    N, M = map(int, raw_input().strip().split())

    bd = [['.'] * N for i in xrange(N)]

    for i in xrange(M):
        ch, R, C = raw_input().strip().split()
        bd[int(R)-1][int(C)-1] = ch

    score, models = rec(0, 0, bd, N, [])
    return score, models


for case in xrange(int(input())):
    score, models = solve()
    print 'Case #%d: %s %d' % (case+1, score, len(models))
    for ch, x, y in models:
        print '%s %d %d' % (ch, x, y)
