def main():
    inp = open("input.txt", "r")
    out = open("output.txt", "w")
    test_count = int(splited_line(inp)[0])
    for x in xrange(1, test_count + 1):
        n = int(splited_line(inp)[0])
        naomi = [float(i) for i in splited_line(inp)]
        ken = [float(i) for i in splited_line(inp)]
        a = solve(n, naomi, ken)
        ans = "Case #%s: %s %s\n"
        # print ans % (x, a[0], a[1])
        out.write(ans % (x, a[0], a[1]))


def solve(n, naomi, ken):
    naomi.sort()
    ken.sort()

    war = 0
    dwar = 0
    cursor_ken = 0
    cursor_naomi = 0

    while cursor_ken < n and cursor_naomi < n:
        if naomi[cursor_naomi] > ken[cursor_ken]:
            cursor_ken += 1
            war += 1
        elif naomi[cursor_naomi] < ken[cursor_ken]:
            cursor_naomi += 1
            cursor_ken += 1

    naomi_rev = list(reversed(naomi))

    while naomi_rev:
        tell = naomi_rev.pop(0)
        ken_play = min_greater(ken, tell)
        naomi_play = min_greater(naomi, ken_play)
        if naomi_play > ken_play:
            dwar += 1
        ken.remove(ken_play)
        naomi.remove(naomi_play)

    return dwar, war


def min_greater(l, m):
    i = [n for n in l if n > m]
    return i[0] if i else min(l)


def splited_line(f):
    return f.readline().strip('\r\n').split(' ')

if __name__ == '__main__':
    main()
