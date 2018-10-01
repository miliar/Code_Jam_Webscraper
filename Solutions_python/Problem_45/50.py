import sys

def find_group(p, cells):
    for c in cells:
        if c[0] <= p and c[1] >= p:
            return c

def split_group(group, p):
    return filter(lambda x: x[0] <= x[1], [[group[0], p-1], [p+1, group[1]]])

def release(lop, occ_cells):
    min = 0
    for i, p in enumerate(lop):
        group = find_group(p, occ_cells) # find the contiguous cells to which p belongs
        cost = group[1] - group[0] # cost of releasing p
        splitted = split_group(group, p)
        new_occ_cells = list(occ_cells)
        new_occ_cells.remove(group)
        new_occ_cells.extend(splitted)
        new_lop = list(lop)
        new_lop.remove(p)
        cost = cost + release(new_lop, new_occ_cells)
        if i == 0: min = cost
        else:
            if cost < min: min = cost
    return min

def ReadInts():
    return list(map(int, sys.stdin.readline().strip().split(" ")))


T = int(raw_input())
for t in range(T):
    P, Q = map(int, raw_input().split())
    cells = [[1, P]]
    prisoners = ReadInts()
    print "Case #%d: %d" % (t+1, release(prisoners, cells))

