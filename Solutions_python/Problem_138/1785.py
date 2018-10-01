import sys
import bisect

get_line = lambda: sys.stdin.readline()

def game_result_fair(n, k):
    if min(n) > max(k):
        return len(n)
    elif min(k) > max(n):
        return 0
    else:
        block = n[0]
        n = n[1:]
        idx = bisect.bisect(k, block)
        k = k[0:idx] + k[idx + 1:]
        return game_result_fair(n, k)

def game_result_deceitful(n, k):
    if min(n) > max(k):
        return len(n)
    elif min(k) > max(n):
        return 0
    elif min(n) > min(k):
        return 1 + game_result_deceitful(n[1:], k[1:])
    elif min(n) < min(k):
        return game_result_deceitful(n[1:], k[:-1])

def solve_case():
    N = int(get_line())
    n = map(lambda x: float(x), get_line().split())
    k = map(lambda x: float(x), get_line().split())
    k.sort()
    n.sort()
    # print "naomi"
    # print n
    # print 'ken'
    # print k
    return " %s %s" % (game_result_deceitful(n, k), game_result_fair(n,k))

def main():
    T = int(get_line())
    for i in xrange(T):
        print "Case #%d:" % (i + 1) + solve_case()

if __name__ == '__main__':
    main()




