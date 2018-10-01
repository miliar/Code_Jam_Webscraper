from copy import copy

def solve_war(blocks):
    score = 0
    skip_one = 0
    for k in xrange(0, 2 * n):
        block = blocks[k]
        if block == 1 and skip_one > 0:
            skip_one -= 1
            continue
        if block == 0:
            skip_one += 1
        else:
            score += 1

    return score

def solve_deceitful_war(blocks):
    score = 0
    skip_zero = 0

    for k in xrange(0, 2 * n):
        block = blocks[k]
        if block == 1:
            skip_zero += 1
            continue

        if skip_zero > 0:
            score += 1
            skip_zero -=1
        else:
            pass

    return score

T = int(raw_input())
for t in xrange(0, T):
    n = int(raw_input())
    naomi_blocks = map(float, raw_input().split())
    ken_blocks = map(float, raw_input().split())
    assert len(naomi_blocks) == n
    assert len(ken_blocks) == n

    naomi_blocks = zip(naomi_blocks, [0] * n)
    ken_blocks = zip(ken_blocks, [1] * n)
    blocks = zip(*sorted(naomi_blocks + ken_blocks))[1]

    print 'Case #%d: %d %d' % (t + 1,
            solve_deceitful_war(blocks), solve_war(blocks))
