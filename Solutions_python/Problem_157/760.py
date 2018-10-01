#! /usr/bin/env python

truth = [
    ["1", "i", "j", "k"],
    ["i", "-1", "k", "-j"],
    ["j", "-k", "-1", "i"],
    ["k", "j", "-i", "-1"]
]


def qmult(a, b):
    mi = (a + b).count("-")

    ai = truth[0].index(a.replace("-", ""))
    bi = truth[0].index(b.replace("-", ""))

    result = truth[ai][bi]
    mn = mi + result.count("-")

    return ("-" if mn % 2 == 1 else "") + result.replace("-", "")


def geninp(chars, x):
    for xi in range(x):
        for c in chars:
            yield c


def find_char(gen, c):
    current = "1"

    i = 0
    while True:
        current = qmult(current, next(gen))
        if current == c:
            yield i

        i += 1


def qmult_all(gen):
    current = "1"

    try:
        while True:
            current = qmult(current, next(gen))
    except:
        pass

    return current


t = int(input())

for ti in range(1, t+1):
    l, x = [int(tmp) for tmp in input().rstrip('\n').split(' ')]
    chars = input().rstrip('\n')
    charslen = l * x
    inp = geninp(chars, x)
    success = False

    ooi = False
    ooj = False

    for io in range(1, charslen):
        if (ooi and ooj) or success:
            break

        for jo in range(1, charslen):
            fi = False
            fj = False
            fk = False

            try:
                gi = find_char(inp, "i")
                for tmp in range(io):
                    next(gi)

                fi = True
            except:
                ooi = True
                break

            try:
                gj = find_char(inp, "j")
                for tmp in range(jo):
                    next(gj)

                fj = True
            except:
                ooj = True
                break

            try:
                fk = (qmult_all(inp) == "k")
            except:
                break

            if fi and fj and fk:
                success = True
                break

    print("Case #{}: {}".format(ti, "YES" if success else "NO"))

