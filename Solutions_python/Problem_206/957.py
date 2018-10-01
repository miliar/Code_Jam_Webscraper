import random

def get_max_time(horses, distance):
    max_time = -1

    for start, speed in horses:
        max_time = max(max_time, (distance - start) / speed)

    return max_time

def main():
    for _ in range(int(input())):
        d, n = [int(x) for x in input().split()]
        horses = [tuple(int(x) for x in input().split()) for _ in range(n)]
        max_time = get_max_time(horses, d)
        print('Case #%d: %.6f' % (_ + 1, d / max_time))

def test():
    N = 1000
    T = 100

    for _ in range(T):
        n, d = N, random.randint(1, 10 ** 9)
        horses = [(random.randint(1, d), random.randint(1, 10000)) for _ in range(n)]
        max_time = get_max_time(horses, d)
        print('Case #%d: %.6f' % (_ + 1, d / max_time))

if __name__ == '__main__':
    main()
