# -*- coding: utf-8 -*-


def tidy(N):
    for i in range(len(N) - 1):
        if N[i] > N[i + 1]:
            return False
    return True


def f(N):
    if len(N) == 1:
        return N

    cand = N[0] + f(N[1:])

    if tidy(cand):
        return cand
    else:
        head = chr(ord(N[0]) - 1)
        return head + '9' * (len(N) - 1)

def main():
    T = int(input())
    for i in range(T):
        x = i + 1

        N = input()
        y = int(f(N))

        print("Case #%d: %d" % (x, y))


if __name__ == '__main__':
    main()
