
def f(T, S, p ,*t):
    assert T == len(t)
    tmp = []
    result = 0
    for v in t:
        r = v % 3
        x = (v - 1) / 3 + 1
        if x >= p:
            result += 1
        elif p == x + 1 and v != 0 and r != 1 and S > 0:
            result += 1
            S -= 1
    return result


def main():
    N = int(raw_input())
    for i in range(N):
        line = map(int, raw_input().split(' '))
        print "Case #{0}: {1}".format(i+1, f(*line))


if __name__ == "__main__":
    main()
