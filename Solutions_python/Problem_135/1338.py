def skip(n):
    for i in range(n):
        raw_input()


def read_case():
    row = input()
    skip(row - 1)
    s = set(map(int, raw_input().split()))
    skip(4 - row)
    return s


for t in range(input()):
    print "Case #%s:" % str(t + 1),
    s = read_case().intersection(read_case())
    if len(s) == 0:
        print "Volunteer cheated!"
    elif len(s) == 1:
        print next(iter(s))
    else:
        print "Bad magician!"