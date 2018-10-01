import sys


def evaluate_(counts, depth, max_depth):
    largest = max(counts)
    min_minutes = max_depth

    if depth >= max_depth or largest > max_depth:
        return max_depth

    for x in xrange(largest / 2, 0, -1):
        new_counts = sorted(counts, reverse=True)
        new_counts[0] -= x
        new_counts.append(x)
        minutes = evaluate_(new_counts, depth + 1,
                            min(max_depth, depth + 1 + max(new_counts)))
        if minutes < min_minutes:
            min_minutes = minutes

    return min_minutes


def evaluate(counts):
    return evaluate_(counts, 0, max(counts))


if __name__ == '__main__':
    sys.stdin.readline()  # skip case count
    lines = sys.stdin.readlines()

    for i in xrange(len(lines) / 2):
        counts = map(lambda x: int(x.strip()), lines[2 * i + 1].split(' '))
        print 'Case #{0}: {1}'.format(i + 1, evaluate(counts))
