def flip(s):
    if s == '+':
        return '-'
    return '+'

def pancake(s, k):
    cnt = 0
    l = list(s)
    for i in xrange(len(l)-k+1):
        if l[i] == '-':
            l[i:i+k] = map(flip, l[i:i+k])
            cnt += 1
    if l[-k:] == ['+']*k:
        return cnt
    return "IMPOSSIBLE"
    
def main(fname):
    import os
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):
        s, k = in_fd.readline().strip().split(" ")
        k = int(k)
        out_fd.write("Case #%d: " % (i+1) + str(pancake(s, k)) + "\n")
    in_fd.close()
    out_fd.close()
