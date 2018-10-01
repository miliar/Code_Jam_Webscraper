infile = open('A-small-attempt0.in', 'r')
outfile = open('test.out', 'w')

T = int(infile.readline())


def finish_time(D, horse):
    return (D - horse[0]) / horse[1]

for t in range(1, T + 1):
    D, N = map(int, infile.readline().strip().split())
    horses = [list(map(int, infile.readline().strip().split())) for _ in range(N)]
    horses.sort(key=lambda x: -x[0])
    i, j = 0, 1
    time = (D - horses[0][0]) / horses[0][1]
    if N == 1:
        pass
    else:
        while j < N:
            if finish_time(D, horses[0]) < finish_time(D, horses[1]):
                i += 1
                j += 1
            else:
                j += 1
        time = (D - horses[i][0]) / horses[i][1]
    outfile.write('Case #{}: '.format(t) + str(round(D / time, 6)) + '\n')
