import argparse
import math

parser = argparse.ArgumentParser(description='Google Code Jam 2017')
parser.add_argument('fin')
parser.add_argument('fout')

args = parser.parse_args()

fin = args.fin
fout = args.fout


def solver(N, P, G):
    print(N, P, G)
    if P == 2:
        odd = 0
        ret = 0
        for i in G:
            if i % 2 == 1:
                odd += 1
            if i % 2 == 0:
                ret += 1
            print(odd,ret)
        ret += odd // 2 + odd % 2
    elif P == 3:
        r = [0, 0, 0]
        for i in G:
            r[i % 3] += 1

        m = min(r[1], r[2])
        M = max(r[1], r[2])
        ret = r[0] + m + (M-m) // 3
        if (M-m) % 3 > 0:
            ret += 1
    elif P == 4:
        print('large')
    else:
        print('error')
    return ret


with open(fin, 'r') as input, open(fout, 'w') as output:
    T = int(input.readline().rstrip('\n'))
    for i in range(0, T):
        s = input.readline().rstrip('\n')
        l = s.split(' ')
        N = int(l[0])  # N, R, O, Y, G, B, and V.
        P = int(l[1])
        s = input.readline().rstrip('\n')
        l = s.split(' ')
        G = [int(i) for i in l]
        answer = 'Case #{}: {}\n'.format(i + 1, solver(N, P, G))
        # print(answer)
        output.write(answer)
