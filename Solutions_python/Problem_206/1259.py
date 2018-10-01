def main():
    filename = "A-large.in"
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]

    # N = int(lines[0])
    lines = lines[1:]
    case = 1
    while len(lines) > 0:
        # D, N
        D, N = [int(line) for line in lines[0].split(' ')]

        times = []
        for i in range(0, N):
            position, speed = [int(line) for line in lines[1 + i].split(' ')]
            times.append((D - position) * 1.0 / speed)

        print "Case #{0}: {1:.6f}".format(case, D / max(times))

        case += 1
        lines = lines[1 + N:]


main()
