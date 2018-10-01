#!/usr/bin/env python

class Group(object):
    def __init__(self, size):
        self.size = size
        self.i = 0
        self.next = None
        self.last_visit = 0
        self.next_head = None
        self.last_total = 0
        self.last_ride = 0

    def __str__(self):
        return "(%s, %s)" % (self.i, self.size)


class RideQueue(object):
    def __init__(self, group_list):
        self._make_queue(group_list)
        self.len = len(group_list)

    def __str__(self):
        s = str(self.head)
        curr = self.head.next
        while curr != self.head:
            s += " => %s" % curr
            curr = curr.next
        return s

    def __len__(self):
        return self.len

    def _make_queue(self, group_list):
        '''Precondition: group_list must be non-empty.'''
        i = 0
        self.head = Group(group_list[0])
        curr = self.head
        curr.i = i
        for size in group_list[1:]:
            curr.next = Group(size)
            curr = curr.next
            i += 1
            curr.i = i
        curr.next = self.head

    def peek(self):
        return self.head.size

    def pop(self):
        res = self.head.size
        self.head = self.head.next
        return res

    def ride(self, k):
        '''Fill the coaster with at most k people and return the euros
        collected.'''
        old_head = self.head
        euros = 0
        if self.peek() <= k:
            p = self.pop()
            euros += p
            k -= p

        while self.peek() <= k and self.head != old_head:
            p = self.pop()
            euros += p
            k -= p

        return euros

class TestRide(object):
    def __init__(self, R, k, group_list):
        self.num_runs = R
        self.people_per_run = k
        self.q = RideQueue(group_list)

    def run_test(self):
        euros = 0
        rides = {}
        r = self.num_runs
        loop_size = 0
        loops = 0
        while r > 0:
            h = self.q.head.i
            if h in rides:
                ride_euros = rides[h].last_ride
                self.q.head = rides[h].next_head
                loop_size =  rides[h].last_visit - r
                loops = r / loop_size

                if loops:
                    # find how much we made since we were last here
                    loop_euros = euros - rides[h].last_total

                    r = r - loop_size * loops
                    if r == 0:
                        euros += loops * loop_euros
                        break
                    # we'll make that much again
                    ride_euros += loops * loop_euros

            else:
                rides[h] = self.q.head
                ride_euros = self.q.ride(self.people_per_run)
                #rides[h] = (ride_euros, r, euros, self.q.head)
                rides[h].next_head = self.q.head
                rides[h].last_total = euros
                rides[h].last_visit = r
                rides[h].last_ride = ride_euros
            euros += ride_euros
            r -= 1

#        print rides
        #print loop_size, loops
        return euros

def main(f_name):
    f = open(f_name, 'r')
    f.readline()

    i = 0

    line_a = f.readline()
    line_b = f.readline()
    while line_a and line_b:# and i < 10:
        i += 1
        R, k, N = [int(x) for x in line_a.strip().split()]
        groups = [int(x) for x in line_b.strip().split()]
        t = TestRide(R, k, groups)
        #print t.q
        print "Case #%s: %s" % (i, t.run_test())
        #print t.q

        line_a = f.readline()
        line_b = f.readline()

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
#    print RideQueue([3,2,1,0])
