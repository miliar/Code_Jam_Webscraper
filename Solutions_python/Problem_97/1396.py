import sys
from collections import deque

def get_range_set(a, b):
    s = set([str(xx) for xx in range(a,b+1)])
    #print s
    return s

def find_recycled(a, b):
    r_set = get_range_set(a, b)
    sol_set = set()
    for xx in range(a, b+1):
        ll = deque([yy for yy in str(xx)])
        for jj in range(len(ll)-1):
            ll.appendleft(ll.pop())
            target = ''.join(ll)
            if int(target) != xx and target in r_set:
                sol_pair = tuple(sorted([xx, int(target)]))
                if sol_pair not in sol_set:    
                    sol_set.add(sol_pair)
    return len(sol_set)

def read_input(fh):
    lines = fh.readlines()[1:]
    idx = 1
    for line in lines:
        a, b = [int(xx) for xx in line.split()]
        num = find_recycled(a, b)
        print "Case #%d: %d" % (idx, num)
        idx += 1

if __name__ == '__main__':
    read_input(sys.stdin)
