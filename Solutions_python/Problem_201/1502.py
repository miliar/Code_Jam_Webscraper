import math
import sys


def get_distances(n, depth):
    distances = {n: 1}  # distance -> cnt
    for i in xrange(1, depth + 1):
        new = {}
        for d, c in distances.iteritems():
            if d < 2:
                continue
            d1 = d2 = d / 2
            if d % 2 == 0:
                d1 -= 1
            if d1:
                new[d1] = new.get(d1, 0) + c
            new[d2] = new.get(d2, 0) + c
        if not new:
            break
        assert(len(new) in (1,2))
        distances = new
    return (max(distances.iteritems()), min(distances.iteritems()))    # (large_dist, cnt), (small_dist, cnt)


def process(n, k):
    level = int(math.log(k)/math.log(2))
    k2 = k - 2**level + 1
    (large_d, large_d_cnt), (small_d, small_d_cnt) = get_distances(n, level)
    window_size = small_d if k2 > large_d_cnt else large_d
    half_size = window_size/2    
    if window_size % 2 == 0:
        return half_size, (half_size - 1)
    else:
        return half_size, half_size


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      n, k = map(int, raw_input().split())
      ma, mi = process(n, k)
      print "Case #{}: {} {}".format(i, ma, mi)
      sys.stdout.flush()


def test(n, k):
    print process(n, k)


if __name__ == "__main__":
    main()
#    import sys
#    test(int(sys.argv[1]), int(sys.argv[2]))

#    for i in xrange(1, 10):
#        print get_distances(230, i) 
