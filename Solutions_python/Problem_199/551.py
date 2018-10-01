def pancake(s):
    cakes, size = s.split(" ")
    cakes = list(cakes)
    count = 0

    for i in range(len(cakes) - int(size) + 1):
        if cakes[i] == '+':
            continue
        else:
            for j in range(int(size)):
                cakes[i + j] = '+' if cakes[i + j] == '-' else '-'
            count += 1
    for i in range(len(cakes) - int(size) + 1, len(cakes)):
        if cakes[i] == '-':
            return "IMPOSSIBLE"

    return str(count)


def main():
    l = int(input())
    for i in range(l):
        result = pancake(input())
        print("Case #{}: {}".format(i + 1, result))


main()