#!/usr/bin/python

def getMid(interval):
    return int((interval[0] + interval[1]) // 2)

def criteria(p):
    midP = getMid(p)

    dlP = midP - p[0]
    drP = p[1] - midP

    return (min(dlP, drP), max(dlP, drP), -midP)


def solve(k, lo, hi):
    intervals = [(lo, hi)]

    for user in range(k):
        intervals = sorted(intervals, key=criteria)

        chosenInterval = intervals[-1]
        intervals.pop()

        mid = getMid(chosenInterval)

        if mid - chosenInterval[0] > 1:
            intervals.append((chosenInterval[0], mid))

        if chosenInterval[1] - mid > 1:
            intervals.append((mid, chosenInterval[1]))

        if user == k-1:
            dl = mid - chosenInterval[0] - 1
            dr = chosenInterval[1] - mid - 1

            return (max(dl, dr), min(dl, dr))


def main():
    for t in range(int(input())):
        n, k = map(int, input().split())

        sol = solve(k, 0, n+1)
        print("Case #%i: %i %i" % (t+1, sol[0], sol[1]))



if __name__ == '__main__':
    main()






