import sys

def play_fair(ken, naomi):
    score = 0
    for b in naomi:
        # find first higher
        higher = -1
        for i in range(len(ken)):
            if ken[i] > b:
                higher = i
                break
        if higher > -1:
            ken.pop(higher)
        else:
            ken.pop(0)
            score += 1
    return score

def play_deceit(ken, naomi):
    score = 0
    while len(naomi) > 0:
        # first first block naomi is not sure to win
        first_lose = -1
        for i in range(len(naomi) - 1, -1, -1):
            if ken[i] > naomi[i]:
                first_lose = i
                break

        if first_lose == -1:
            score += len(naomi)
            return score
        else:
            ken.pop(first_lose)
            naomi.pop(0)
    return score

def process_case():
    N = int(sys.stdin.readline())
    naomi = [float(x) for x in sys.stdin.readline().strip().split(' ')]
    ken = [float(x) for x in sys.stdin.readline().strip().split(' ')]

    naomi.sort()
    ken.sort()

    score_fair = play_fair(list(ken), list(naomi))
    score_deceit = play_deceit(ken, naomi)

    return '%d %d' % (score_deceit, score_fair)

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        result = process_case()
        print 'Case #%d: %s' % (i + 1, result)

if __name__ == '__main__':
    main()
