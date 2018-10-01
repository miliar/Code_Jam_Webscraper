def number_of_flips(s, k):
    k = int(k)
    s = s.replace('+', '1').replace('-', '0')
    a = map(bool, map(int, list(s)))
    flips = 0
    for i in xrange(len(a) - k + 1):
        print flips, a
        if not a[i]:
            flips += 1
            for j in xrange(i, i + k):
                a[j] = not a[j]
        if all(a):
            return flips
    return 'IMPOSSIBLE'


def process(filename):
    answers = []
    with open(filename + '.in') as f:
        lines = tuple(f.readlines())
    cases = int(lines[0])
    for x in range(1, cases + 1):
        s, k = lines[x].split()
        answers.append('Case #{}: {}'.format(x, number_of_flips(s, k)))
    with open(filename + '.out', 'w') as f:
        f.write('\n'.join(answers))


if __name__ == '__main__':
    process('A-sample')
    process('A-small-attempt0')
    process('A-large')
