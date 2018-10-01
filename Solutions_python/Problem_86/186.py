import fileinput


def solve(notes, L, H):

    for f in range(L, H+1):
        for n in notes:
            if not (f % n == 0 or n % f == 0):
                break
        else:
            return f
    return 'NO'

readline = fileinput.input().readline
case_count = int(readline())
for case_no in range(case_count):
    N, L, H = [int(x) for x in readline().split()]
    notes = [int(x) for x in readline().split()]
    answer = solve(notes, L, H)
    print "Case #%d: %s" % (case_no+1, answer)
