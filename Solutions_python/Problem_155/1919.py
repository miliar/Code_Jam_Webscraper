__author__ = 'apetresc'

def solve(Sm, S):
    needed = 0
    people_clapping = S[0]
    for i in range(0, Sm):
        while people_clapping < i + 1:
            needed += 1
            people_clapping += 1
        people_clapping += S[i + 1]

    return needed


if __name__ == '__main__':
    f = open('A-large.in', 'r')
    T = int(f.readline())
    for i in range(T):
        l = f.readline().strip()
        Sm, S = (lambda x: (int(x[0]), [int(c) for c in x[1]]))(l.split())

        print "Case #%d: %d" % (i + 1, solve(Sm, S))
