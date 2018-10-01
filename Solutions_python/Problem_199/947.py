def o(s):
    if s == '-':
        return '+'
    return '-'

def isHappy(s):
    for c in list(s):
        if c == '-':
            return False
    return True

def flip(s, i, k):
    a = list(s)
    for j in range(i, i + k):
        a[j] = o(a[j])
    return ''.join(a)

def solve(s, k):
    if isHappy(s):
        return 0

    visited = set()
    jobs = list()
    jobs.append({ 's': s, 'd': 0 })

    while True:
        newJobs = []
        for job in jobs:
            for i in range(0, len(s) - k + 1):
                ss = flip(job['s'], i, k)

                if ss in visited:
                    continue

                if isHappy(ss):
                    return str(job['d'] + 1)

                visited.add(ss)
                newJobs.append({ 's': ss, 'd': job['d'] + 1 })
        if len(newJobs) < 1:
            return 'IMPOSSIBLE'
        jobs = newJobs

t = int(raw_input())
for i in range(1, t + 1):
    n, k = [str(s) for s in raw_input().split(' ')]
    print('Case #{}: {}'.format(i, solve(n, int(k))))
