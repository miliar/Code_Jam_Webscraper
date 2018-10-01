# https://code.google.com/codejam/contest/3264486/dashboard#s=p2
import llist


def check(s, l, r, far_from_neighbors, head):
    L = s - l - 1
    R = r - s - 1
    mn = min(L, R)
    mx = max(L, R)
    existing_mn = far_from_neighbors['mn']
    if existing_mn > mn:
        return
    if existing_mn < mn:
        far_from_neighbors['mn'] = mn
        far_from_neighbors['mx'] = mx
        far_from_neighbors['s'] = [s, head]
        return

    existing_mx = far_from_neighbors['mx']
    if existing_mx > mx:
        return
    if existing_mx < mx:
        far_from_neighbors['mx'] = mx
        far_from_neighbors['s'] = [s, head]
        return

    # use left-most
    if far_from_neighbors['s']:
        return
    far_from_neighbors['s'] = [s, head]


def find_spot(dl, ki):
    head = dl.first
    tail = dl.last
    far_from_neighbors = {'mn': 0, 'mx': 0, 's': None}
    while head != tail:
        s1 = (head.value + head.next.value) // 2
        if s1 != head.value:
            check(s1, head.value, head.next.value, far_from_neighbors, head.next)
            s2 = s1 + 1
            if s2 != head.next.value:
                check(s2, head.value, head.next.value, far_from_neighbors, head.next)
        head = head.next
    # print far_from_neighbors
    # assert far_from_neighbors['s'] is not None
    # assert far_from_neighbors['s']
    dl.insert(far_from_neighbors['s'][0], far_from_neighbors['s'][1])
    return far_from_neighbors['mx'], far_from_neighbors['mn']


def solve(n, k):
    dl = llist.dllist()
    dl.appendleft(0)
    dl.append(n + 1)

    for ki in xrange(k):
        mx, mn = find_spot(dl, ki)
    # print mx, mn

    return mx, mn


def get_input(lines):
    out = []
    for i in xrange(1, len(lines)):
        print "line %s / %s" % (i, len(lines) - 1)
        if not lines[i]:
            continue
        n, k = lines[i].strip().split()
        mx, mn = solve(int(n), int(k))
        out.append("Case #%s: %s %s\n" % (i, mx, mn))
    return out


fin_name = "C-small-1-attempt0.in"
fout_name = fin_name + ".out"
with open(fin_name) as fin:
    with open(fout_name, "w") as fout:
        fout.writelines(get_input(fin.readlines()))
        print "done, written to %s" % fout_name
