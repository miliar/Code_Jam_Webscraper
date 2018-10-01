if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        ps = raw_input().split()[1:]

        events = []
        for i in xrange(0, len(ps), 2):
            events += [(ps[i], ps[i + 1])]

        pos = {'O': 1, 'B': 1}

        p = 0
        wait = 0
        total = 0
        while p < len(events):
            rob, x = events[p][0], int(events[p][1])
            dist = abs(pos[rob] - x)
            if p and rob == events[p - 1][0]:
                t = 1 + dist
                total += t
                wait += t
                pos[rob] = x
            else:
                t = 1 + max(0, dist - wait)
                total += t
                wait = t
                pos[rob] = x

            p += 1


        print 'Case #%d: %d' % (caseno + 1, total)

