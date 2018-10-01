from collections import defaultdict

def solve(n, k):
    gaps = defaultdict(int)
    gaps[n] = 1
    for _ in range(k):
        # person comes in, looks at largest gap
        largest_gap = max(gaps.keys())
        y = largest_gap // 2
        z = y - (not (largest_gap % 2))
        gaps[largest_gap] -= 1
        if gaps[largest_gap] == 0:
            del gaps[largest_gap]
        gaps[y] += 1
        gaps[z] += 1
    return '{} {}'.format(y, z)

def solve2(n, k):
    gaps = defaultdict(int)
    gaps[n] = 1
    people_entered = 0
    while people_entered < k:
        # person comes in, looks at largest gap
        largest_gap, num_people = max(gaps.items())
        y = largest_gap // 2
        z = y - (not (largest_gap % 2))
        del gaps[largest_gap]
        gaps[y] += num_people
        gaps[z] += num_people
        people_entered += num_people

    return '{} {}'.format(y, z)

if __name__ == '__main__':
    import io
    for i, line in enumerate(io.open('C-large.in', 'r').readlines()):
        if i == 0: continue
        n, k = line.split()
        n = int(n)
        k = int(k)
        print('Case #{}: {}'.format(i, solve2(n, k)))
