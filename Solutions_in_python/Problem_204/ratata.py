from collections import defaultdict

def get_valid_range(w, p):
    c = p/w
    while c*w*1.1 >= p:
        c -= 1
    c += 1
    if c*w*0.9 > p:
        return (0, 0)
    low = c
    while c*w*0.9 <= p:
        c += 1
    return (low, c-1)

def ratata(n, p, w, np_mat):
    d = dict()
    for i in xrange(n):
        for j in xrange(p):
            low, high = get_valid_range(w[i], np_mat[i][j])
            if low == 0:
                continue
##            print j, low, ":", high,
            for k in xrange(low, high+1):
                if k in d:
                    d[k][i].add(j)
                else:
                    d[k] = defaultdict(set)
                    d[k][i].add(j)
##            print
    exclude_ids = defaultdict(set)
    packages = 0
    for k in d.iterkeys():
        while len(d[k].keys()) == len(w):
            local_exclude = defaultdict(set)
##            print k, d[k]
            package_size = 0
            for i in xrange(n):
                d[k][i] -= exclude_ids[i]
##                print k, d[k]
                if d[k][i]:
                    package_size += 1
                    local_exclude[i].add(d[k][i].pop())
                    if not d[k][i]:
                        del d[k][i]
                else:
                    del d[k][i]
            if package_size == n:
                packages += 1
                for i in xrange(n):
##                    print i, local_exclude[i]
                    exclude_ids[i].update(local_exclude[i])
##                print exclude_ids
            else:
                break
    return packages
    

def main(fname):
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):
        n, p = map(int, in_fd.readline().strip().split(" "))
        w = map(int, in_fd.readline().strip().split(" "))
        np_mat = []
        for j in xrange(n):
            np_mat.append(sorted(map(int, in_fd.readline().strip().split(" "))))
        out_fd.write("Case #%d: " % (i+1) + str(ratata(n, p, w, np_mat)) + "\n")
    in_fd.close()
    out_fd.close()

