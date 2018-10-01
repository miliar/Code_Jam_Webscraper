def main():
    file = open('A-large.in.txt', 'r')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToList(file.readline())
        # print(line)
        extras = solve(line)
        output = "Case #" + str(x + 1) + ": " + str(extras)
        print(output)


def solve(line):
    max = int(line[0])
    input = line[1]
    current = 0
    extras = 0
    for x in range(max):
        count = int(input[x:(x+1)])
        # print("count: " + str(count))
        current = current + count
        # print("current: " + str(current))
        nextCount = x+1

        # print("nextCount: " + str(nextCount))
        if current < nextCount:
            added = (nextCount - current)
            current = current + added
            extras = extras + added
            # print("extras " + str(extras))
        # print
    return extras


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()

if __name__ == '__main__':
    main()
