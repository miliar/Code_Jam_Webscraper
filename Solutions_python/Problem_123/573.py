
from collections import deque


def reduce(curr, motes):
    for i, mote in enumerate(motes):
        if curr > mote:
            curr += mote
        else:
            return curr, motes[i:]
    return curr, []


def handle(A, N, others):
    q = deque([(0, A, others)])
    result = None

    while q:
        count, curr, motes = q.popleft()

        nxt, rest = reduce(curr, motes)
        n = len(rest)

        if n == 0:
            if result is None or count < result:
                result = count
        elif n == 1:
            if result is None or count + 1 < result:
                result = count + 1

        else:
            q.append((count + 1, nxt, [nxt - 1] + rest))
            q.append((count + 1, nxt, rest[1:]))

        if result:
            q_ = deque()
            for count, curr, motes in q:
                if count < result:
                    q_.append((count, curr, motes))

            q = q_

    return result

for case in xrange(int(raw_input())):
    parts = [int(x) for x in raw_input().split()]
    A = parts[0]
    N = parts[1]
    others = sorted([int(x) for x in raw_input().split()])
    print 'Case #%d: %s' % (case + 1, handle(A, N, others))

