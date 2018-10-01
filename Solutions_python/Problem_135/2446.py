def read_data():
    a = int(raw_input())
    for i in [1, 2, 3, 4]:
        d = map(int, raw_input().split(" "))
        if a == i:
            ret = d
    return ret


def solve():
    s = set(read_data()) & set(read_data())
    if len(s) == 1:
        return s.pop()
    elif len(s) >= 2:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"


T = int(raw_input())
for x in range(1, T+1):
    print "Case #%d:" % x, solve()
