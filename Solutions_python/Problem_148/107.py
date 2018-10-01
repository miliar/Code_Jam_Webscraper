
import sys

def solve(case, f):
    n, x = map(int, f.readline().split())
    a = map(int, f.readline().split())
    a.sort()
    a.reverse()
  #  print a
    count = 0
    last = n - 1
    for i in xrange(n):
   #     print i, last
        if last < i:
            return count
        if a[last] + a[i] <= x:
            last -= 1
        count += 1
    return count


if __name__ == "__main__":
    f = sys.stdin

    t = int(f.readline())
    for _t in xrange(t):
        rez = solve(_t, f)
        print 'Case #%s: %s' % (_t + 1, rez)
