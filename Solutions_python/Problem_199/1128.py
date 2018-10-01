def all_good(pancakes):
    return all(pancakes)


def flipper(pancakes, k):
    count = 0
    for i in range(len(pancakes) - k + 1):
        if not pancakes[i]:
            count += 1
            for j in range(i, i+k):
                pancakes[j] = not pancakes[j]

        if all_good(pancakes):
            return count

    return "IMPOSSIBLE"


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        data = input().split()
        pancakes = [c == '+' for c in data[0]]
        k = int(data[1])
        print('Case #{t}: {v}'.format(t=i+1, v=flipper(pancakes, k)))
