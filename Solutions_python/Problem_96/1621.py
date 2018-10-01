def main():
    f = open("B-large.in")
    cases = f.readline()
    cur = 1
    for line in f.readlines():
        vec = map(int, line.split())
        print "Case #%d: %d" % (cur, foo(vec[0], vec[1], vec[2], vec[3:]))
        cur += 1
    f.close()

NO_WAY = 0
NO_SURPRISE = 1
SURPRISED = 2

def foo(N, S, p, tis):
    count = 0
    for ti in tis:
        res = bar(ti, p)
        if res == NO_SURPRISE:
            #print "NO SURPRISE: %d has a %d" % (ti, p)
            count += 1
        elif res == SURPRISED and S > 0:
            #print "SURPRISED: %d could have a %d" % (ti, p)
            count += 1
            S -= 1
    return count

def bar(t, p):
    avg = t / 3.0
    if avg > p-1:
        return NO_SURPRISE  # Combo must have p or above
    if t >= p and t >= p * 3 - 4:
        return SURPRISED    # Could have surprising result with >p
    return NO_WAY

if __name__ == "__main__":
    main()
