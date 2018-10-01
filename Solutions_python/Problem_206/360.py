__author__ = 'rutger'


def solve(h, dest):
    maxtime = 0.0

    for horse in h:
        pos = horse[0]
        speed = horse[1]
        delta = dest - pos
        time = delta / speed
        maxtime = max(maxtime, time)

    return dest * 1.0 / maxtime


for T in range(int(input())):
    d, n = list(map(int, input().split(' ')))
    horses = []
    for i in range(n):
        pos, speed = list(map(float, input().split(' ')))
        horses.append((pos * 1.0, speed * 1.0))
    res = solve(horses, d)
    print('Case #%d: %f' % (T + 1, res))