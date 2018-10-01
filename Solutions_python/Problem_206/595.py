INPUT_FILE = __file__.replace('.py', '.input')
OUTPUT_FILE = __file__.replace('.py', '.output')


def solve(d, horses):
    t = max((d-k)/s for k, s in horses)
    return d/t


def main():

    with open(INPUT_FILE, 'r') as f, open(OUTPUT_FILE, 'w') as g:
        t = int(f.readline().strip())
        for i in xrange(1, t+1):
            d, n = map(int, f.readline().strip().split())
            horses = []
            for __ in xrange(n):
                horses.append(map(int, f.readline().strip().split()))
            soln = solve(float(d), horses)
            outline = 'Case #{i}: {soln}\n'.format(**locals())
            g.write(outline)
            print outline,


if __name__ == '__main__':
    main()
