import sys

def comb(n, k):
    if k == 0:
        yield []
    elif n == k:
        yield range(k)
    else:
        for a in comb(n - 1, k):
            yield a
        for a in comb(n - 1, k - 1):
            yield a + [n - 1]

def get_max_score(tri_score, surprising):
    if tri_score == 0:
        return 0
    elif not surprising:
        return (tri_score + 2) / 3
    else:
        if tri_score % 3 == 1:
            return (tri_score + 2) / 3
        else:
            return (tri_score + 2) / 3 + 1
            
limit = int(sys.stdin.readline())

i_line = 1
for i in range(limit):
    lst = map(int, sys.stdin.readline().split(" "))

    N = int(lst[0])
    lst.pop(0)
    S = int(lst[0])
    lst.pop(0)
    p = int(lst[0])
    lst.pop(0)

    max_count = 0
    for S_lst in comb(N, S):
        count = 0
        for i in range(N):
            val = get_max_score(lst[i], (i in S_lst))
            if val >= p:
                count += 1
        if max_count < count:
            max_count = count

    print "Case #" + str(i_line) + ": " + str(max_count)
    i_line += 1
