from collections import Counter

def solve(N, P, G):
    """ solve the problem """

    #print(N, P, G)

    G = [g % P for g in G]
    ans = 0
    if P == 2: 
        c = Counter(G)
        ans += c[0] + int(c[1]/2)
        c[1] %= 2
        if c[1] > 0: ans += 1


    if P == 3:
        c = Counter(G)
        ans += c[0]
        one_with_two = min(c[1], c[2])
        ans += one_with_two
        c[1] -= one_with_two
        c[2] -= one_with_two
        ans += int(c[1]/3) + int(c[2]/3)
        c[1] %= 3
        c[2] %= 3
        if c[1] > 0 or c[2] > 0: ans += 1

    if P == 4:
        c = Counter(G) 
        ans += c[0]
        one_with_three = min(c[1], c[3])
        ans += one_with_three
        c[1] -= one_with_three
        c[3] -= one_with_three
        ans += int(c[2]/2)
        c[2] %= 2
        if c[1] >= 2 and c[2] >= 1:
            c[1] -= 2
            c[2] -= 1
            ans += 1
        if c[3] >= 2 and c[2] >= 1:
            c[3] -= 2
            c[2] -= 1
            ans += 1
        ans += int(c[1] / 4)
        c[1] %= 4
        ans += int(c[3] / 4)
        c[3] %= 4
        if c[1] > 0 or c[2] > 0 or c[3] > 0:
            ans += 1
        

    return ans


def parse():
    """ parse input """

    N, P = [int(i) for i in input().split()]
    G = [int(i) for i in input().split()]

    return N, P, G


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
