import sys


class Solved(Exception):
    pass


def solve(a, b, data, data2):
    result = set(data[a]) & set(data2[b])
    if not result:
        raise Solved('Volunteer cheated!')

    if len(result) == 1:
        raise Solved(list(result)[0])

    raise Solved('Bad magician!')


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        a = int(sys.stdin.readline())
        data = []

        for _ in range(4):
            data.append(map(int, sys.stdin.readline().strip().split(' ')))

        b = int(sys.stdin.readline())
        data2 = []

        for _ in range(4):
            data2.append(map(int, sys.stdin.readline().strip().split(' ')))

        try:
            solve(a-1, b-1, data, data2)
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
