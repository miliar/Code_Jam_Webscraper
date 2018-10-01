def prt(case, n):
    print "Case #%s: %s" % (case + 1, n)

def flip(stack, index, k):
    s = index - k + 1
    e = index + 1

    if s < 0:
        raise IndexError()
    # print stack, s, e
    # print stack[:s], stack[s:e], stack[e:]
    # print stack[:s] + map(lambda x: x ^ 1, stack[s : e]) + stack[e:]
    # print
    return stack[:s] + map(lambda x: x ^ 1, stack[s : e]) + stack[e:]

for case in xrange(int(raw_input())):
    is_impossible = False

    flips = 0
    d = {'+': 1, '-' : 0}
    stack, k = raw_input().split()
    k = int(k)
    stack = map(lambda x: d[x], stack)
    l = len(stack)
    # print stack, k

    for i in range(l)[::-1]:
        if stack[i] == 0:
            try:
                flips += 1
                stack = flip(stack, i, k)
            except Exception:
                is_impossible = True
                break

    # print stack
    if is_impossible:
        prt(case, "IMPOSSIBLE")
    else:
        prt(case, flips)
