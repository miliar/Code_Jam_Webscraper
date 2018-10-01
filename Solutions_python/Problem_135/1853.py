import sys
import bisect

get_line = lambda: sys.stdin.readline()


def solve_case():
    n1 = int(get_line())
    cards1 = [map(lambda x: float(x), get_line().split()) for _ in xrange(4)]
    n2 = int(get_line())
    cards2 = [map(lambda x: float(x), get_line().split()) for _ in xrange(4)]

    insec = set(cards1[n1 -1]) & set(cards2[n2 -1])
    if len(insec) == 1:
        return " %d" % list(insec)[0]
    elif len(insec) == 0:
        return " Volunteer cheated!"
    elif len(insec) > 1:
        return " Bad magician!"


def main():
    T = int(get_line())
    for i in xrange(T):
        print "Case #%d:" % (i + 1) + solve_case()

if __name__ == '__main__':
    main()




