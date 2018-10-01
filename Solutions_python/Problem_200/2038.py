def tolist(n):
    return [int(i) for i in list(str(n))]

def toint(l):
    n = len(l)
    s = 0
    for p, i in enumerate(l):
        s += i * 10 ** (n-p - 1)
    return s

def decrement(n, start):
    n[:start + 1] = tolist(toint(n[:start + 1]) - 1)

    for i in range(start+1, len(n)):
        n[i] = 9

def largest_tidy(n):
    while True:
        i = 0
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                break
        else:
            return toint(n)

        decrement(n, i)

def main():
    N = int(input())
    for t in range(1, N + 1):
        n = [int(i) for i in input()]
        print("Case #%d: %s" % (t, largest_tidy(n)))

main()
