import math

if __name__ == "__main__":
    case = 1

    with open('input.txt', 'r') as f:
        content = f.readlines()
        cases = int(content[0])

    content = [c.rstrip() for c in content]

    while case <= cases:
        r, t = map(int, list(content[case].split()))
        x = 4 * r * r + 1 - 4 * r + 8 * t
        y = 1 - 2 * r
        z = math.sqrt(x)
        y = y + z
        m = int(y/4)

        print "Case #%d: %d" % (case, m)
        case += 1