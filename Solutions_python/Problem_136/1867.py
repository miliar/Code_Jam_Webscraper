#!/usr/bin/env python3

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        C, F, X = map(float, input().split())

        cps = 2.
        best = X/cps
        time = C/cps

        while time < best:
            # buying a new farm
            cps += F
            best = min(best, time + X/cps)
            time += C/cps

        print('Case #{}: {:.16f}'.format(t, best))
