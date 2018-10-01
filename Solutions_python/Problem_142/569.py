def reduce_s(s):
    reduced = s[0]
    for si in range(1, len(s)):
        if s[si] != s[si - 1]:
            reduced += s[si]
    return reduced


def f(s):
    reduced = []
    tmp = s[0]
    for si in range(1, len(s)):
        if s[si - 1] == s[si]:
            tmp += s[si]
        else:
            reduced.append(tmp)
            tmp = s[si]
    reduced.append(tmp)
    return reduced


def g(num, part):
    sums = 0
    for w in part:
        sums += abs(len(w) - num)
    #print num, part, sums
    return sums


def solve():
    N = int(raw_input())
    words = [raw_input() for _ in range(N)]
    reduced_ws = [reduce_s(w) for w in words]
    total = 0
    if any((w != reduced_ws[0]) for w in reduced_ws):
        return "Fegla Won"
    else:
        cool_ws = [f(w) for w in words]
        #print cool_ws
        for j in range(len(cool_ws[0])):
            sums = 0
            part_ws = []
            for i in range(len(cool_ws)):
                #print cool_ws[i][j]
                sums += len(cool_ws[i][j])
                part_ws.append(cool_ws[i][j])
            total += g(int(round(float(sums) / len(words))), part_ws)
        return total


if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1, T + 1):
        out = solve()
        print "Case #{}: {}".format(t, out)
