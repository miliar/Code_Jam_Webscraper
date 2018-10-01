translation = {ord('+'): '-', ord('-'): '+'}


def neighbours(s, k):
    for i in range(0, len(s) - k + 1):
        yield s[:i] + s[i: i + k].translate(translation) + s[i + k:]


def bfs(s, k):
    # Let's try with a good ol' BFS
    to_explore = [(0, s)]
    explored = set()
    goal = '+' * len(s)

    while to_explore:
        (cost, state) = to_explore.pop(0)

        if state == goal:
            return cost

        if state not in explored:
            explored.add(state)
            for neighbour in neighbours(state, k):
                to_explore.append((cost + 1, neighbour))

    return 'IMPOSSIBLE'


t = int(input())
for i in range(1, t + 1):
    s, k = input().split(' ')
    k = int(k)

    cost = bfs(s, k)
    print("Case #{}: {}".format(i, cost))
