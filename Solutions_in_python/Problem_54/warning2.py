
import sys
import fractions

def get_diffs_gcd(times):
    ret = 0
    diffs = []
    for i in xrange(len(times)):
        current = times[i]
        for t in times:
            if t != current:
                diffs.append(abs(current-t))
    if diffs:
        ret = reduce(fractions.gcd, diffs)
    return ret


if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        line = stdin.readline()
        parse_nums = map(int, line.split())
        N = parse_nums[0]
        times = parse_nums[1:]

        diffs_gcd = get_diffs_gcd(times)
        min_time = min(times)

        if min_time % diffs_gcd == 0:
            test = 0
        else:
            start_factor = (min_time / diffs_gcd) + 1
            test = (diffs_gcd * start_factor) - min_time

        print "Case #%d: %d" % (i+1, test)
