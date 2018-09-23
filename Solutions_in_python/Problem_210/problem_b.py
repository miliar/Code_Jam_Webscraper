from collections import deque  # @UnresolvedImport
from sys import stdin

DEBUG = False

def main():
    t = int(stdin.readline().strip())
    for k in xrange(1, t+1):
        ac, aj = (int(s) for s in stdin.readline().strip().split(' '))
        cd = [[int(s) for s in stdin.readline().strip().split(' ')]
              for _ in xrange(ac)]
        jk = [[int(s) for s in stdin.readline().strip().split(' ')]
              for _ in xrange(aj)]
        time = [0, 0]
        count = 0
        slots = [[], []]
        data = sorted([(start, stop, 0) for start, stop in cd] + [(start, stop, 1) for start, stop in jk])
        if not data:
            if DEBUG:
                print "Case #{}: 2".format(k)
            continue
        last_stop = data[-1][1] - 1440
        last_who = data[-1][2]
        buf = 0
        for start, stop, who in data:
            if DEBUG:
                print "{} {} {}".format(start, stop, who)
            if who != last_who:
                if DEBUG:
                    print "Between {} and {} switch from {} to {}".format(last_stop, start, last_who, who)
                last_who = who
                count += 1
                if start != last_stop:
                    if DEBUG:
                        print "Inc buf from {} to {}".format(buf, buf + (start-last_stop))
                    buf += start - last_stop
            else:
                if start != last_stop:
                    slots[who].append(start - last_stop)
            time[who] += stop - start
            last_stop = stop
        if DEBUG:
            print "buf {}, count {}".format(buf, count)
        count += count & 1
        for who in xrange(2):
            # Consume own slots
            slots[who] = deque(sorted(slots[who]))
            while slots[who] and time[who] + buf < 720:
                if DEBUG:
                    print "A {} is still {} {} problematic".format(who, time[who], buf)
                if slots[who][0] > 720 - (time[who] + buf):
                    slots[who][0] -= 720 - (time[who] + buf)
                    time[who] = 720 - buf
                else:
                    time[who] += slots[who].popleft()
        for who in xrange(2):
            while slots[1-who] and time[who] + buf < 720:
                if DEBUG:
                    print "B {} is still {} {} problematic".format(who, time[who], buf)
                count += 2
                if slots[1-who][-1] > 720 - (time[who] + buf):
                    slots[1-who][-1] -= 720 - (time[who] + buf)
                    time[who] = 720 - buf
                else:
                    time[who] += slots[1-who].popleft()
        print "Case #{}: {}".format(k, count)
        if DEBUG:
            print ""

main()
