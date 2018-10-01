import sys

# 1. how long would it take to wait for X cookies to be created.
# 2. how long would it take to build one more farm and then wait for X cookies
# to be created.
# return (1) when it is the smaller of the two.


def solve_test(c, f, x, rate, time_so_far):
    # time if we just wait
    waittime = x / rate
    # time to build another farm
    buildtime = c / rate
    totalbuildtime = buildtime + x / (rate + f)
    while waittime > totalbuildtime:
        # choose to build
        rate = rate + f
        time_so_far = time_so_far + buildtime
        waittime = x / rate
        buildtime = c / rate
        totalbuildtime = buildtime + x / (rate + f)
    return time_so_far + waittime

if __name__ == "__main__":
    lines = [line.rstrip('\n') for line in open(sys.argv[1])]
    f = open('out.txt', 'w')
    test_number = 1
    for line in lines[1:]:
        ln = [float(i) for i in line.split(" ")]
        f.write('Case #%s: %s\n' % (test_number, round(solve_test(ln[0], ln[1], ln[2], 2, 0), 7)))
        test_number += 1
    f.close()
