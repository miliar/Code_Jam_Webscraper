def rollercoaster(rides, size, queue):
    profit, aboard = 0, 0
    while rides:
        i, aboard = 0, 0
        for x in queue:
            if aboard + x > size:
                break
            i, aboard = i + 1, aboard + x
        profit += aboard
        queue = queue[i:] + queue[:i]
        rides -= 1
    return profit

def main():
    try:
        cases = xrange(1, int(raw_input())+1)
        for case in cases:
            rides, size, queue_len = map(int, raw_input().split())
            queue = map(int, raw_input().split())
            assert queue_len == len(queue)
            print "Case #%d: %d" % (case, rollercoaster(rides, size, queue))
    except:
        print "INVALID INPUT"

main()
