
def get_answer(s, k):

    size = len(s)
    goal = pow(2, size) - 1
    mask = pow(2, k) - 1

    head = 0
    for c in s:
        head <<= 1
        if c == '+':
            head += 1

    if head == goal:
        return 0

    visited = set([head])

    count = 0
    queue = [head, None]
    while queue:
        curr = queue.pop(0)
        if curr is None :
            count += 1
            if not queue:
                break
            queue.append(None)
            continue

        for i in range(size - k + 1):
            m = mask << i
            nxt = m ^ curr
            if nxt == goal:
                return count + 1
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

    return 'IMPOSSIBLE'

t = int(input())
for i in range(1, t + 1):

    s, k = input().split(" ")
    k = int(k)

    answer = get_answer(s, k)
    print("Case #{}: {}".format(i, answer))

