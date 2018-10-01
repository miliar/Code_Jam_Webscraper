
def check(levels):
    standing = 0
    for shyness, number in enumerate(levels):
        if standing >= shyness:
            standing += number
    return standing == sum(levels)

def solve(levels):
    extra = 0
    while True:
        new_levels = levels[:]
        new_levels[0] += extra
        if check(new_levels):
            return extra
        extra += 1

if __name__ == "__main__":
    count = int(raw_input())
    for case in xrange(1, count + 1):
        parts = raw_input().split(" ")
        levels = [int(i) for i in parts[1]]
        print "Case #%s: %s" % (case, solve(levels))
