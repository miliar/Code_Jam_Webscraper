def split(N):
    DX1, DX2 = N/2, (N-1)/2
    N2 = (N-1)/2
    N1 = N - N2 - 1

    return (DX1, DX2), (N1, N2)

DEBUG=0

def solve(N, K):
    cur = K
    rooms = {N: 1}
    step = 0
    while cur > 0:
        step += 1
        if DEBUG:
            print 'rooms:', sorted(rooms.items()), 'at step', step
        key = max(rooms.keys())
        val = rooms[key]
        del rooms[key]
        cur -= val
        (Dmax, Dmin), (N1, N2) = split(key)
        if DEBUG:
            print ' splitted', key, 'and got',
            print '(Dmax, Dmin), (N1, N2) = %s, %s' % ((Dmax, Dmin), (N1, N2))
            print ' -> %d left' % cur
        if N1 not in rooms:
            rooms[N1] = 0
        if N2 not in rooms:
            rooms[N2] = 0
        rooms[N1] += val
        rooms[N2] += val
    return Dmax, Dmin


def main():
    T = input()

    for i in range(T):
        N, K = map(int, raw_input().split())
        print 'Case #{}:'.format(i+1), '%d %d' % solve(N, K)

if __name__ == '__main__':
     main()
