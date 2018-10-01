import sys

def solve(a1, cards1, a2, cards2):
    poss1 = set(cards1[a1-1])
    poss2 = set(cards2[a2-1])
    poss = poss1.intersection(poss2)
    if len(poss) == 0:
        return 'Volunteer cheated!'
    if len(poss) > 1:
        return 'Bad magician!'
    return list(poss)[0]

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        a1 = int(sys.stdin.readline())
        cards1 = []
        for j in range(4):
            cards1.append(map(int, sys.stdin.readline().split(' ')))
        a2 = int(sys.stdin.readline())
        cards2 = []
        for j in range(4):
            cards2.append(map(int, sys.stdin.readline().split(' ')))
        answer = solve(a1, cards1, a2, cards2)
        print 'Case #{}: {}'.format(i+1, answer)

if __name__ == '__main__':
    main()
