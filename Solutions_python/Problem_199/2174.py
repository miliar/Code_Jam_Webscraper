def parse(fi):
    f = open(fi)
    return map(lambda x: x[:-1],f.readlines())


def problem():
    data = parse("pancake/paninput.txt")
    for b in range(len(data[1:])):
        i = data[1:][b]
        i = i.split()
        k = int(i[1])

        # +'s
        s = list(i[0])
        n2 = 0
        for j in range(len(s) - k + 1):
            if s[j] != '+':
                for l in range(k):
                    if s[j+l] == '-':
                        s[j+l] = '+'
                    else:
                        s[j+l] = '-'
                n2 += 1
        for a in s:
            if a == '-':
                n2 = -1
                break

        if n2 == -1:
            print "Case #" + str(b+1) + ": IMPOSSIBLE"
        else:
            print "Case #" + str(b+1) + ": " + str(n2)





problem()
