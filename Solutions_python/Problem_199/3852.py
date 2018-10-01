import sys

def successors(state, K):
    s = state[0]
    n = state[1]
    return [(flip(s, pos, K), n + 1) for pos in range(len(s) - K + 1)]

def flip(state, pos, K):
    return "".join([state[i] if i < pos or i >= pos + K else neg(state[i]) for i in range(len(state))])

def neg(bit):
    return "+" if bit == "-" else "-"

def bfs(start, K):
    def bfs_iter(queue, path, K):
        state = queue.pop(0)
        if state[0] in path:
            return
        path.append(state[0])
        if allpos(state[0]):
            return state
        for s in successors(state, K):
            queue.append(s)
        return
    queue = [(start, 0)]
    path = []
    while len(queue) > 0:
        found = bfs_iter(queue, path, K)
        if found:
            return found[1]
    return -1

def allpos(state):
    return "-" not in state

def tests():
    test_successors()
    test_bfs()

def test_successors():
    assert successors(("+", 0), 1) == [("-", 1)]
    assert successors(("++", 0), 1) == [("-+", 1), ("+-", 1)]

def test_bfs():
    assert bfs("+", 1) == 0
    assert bfs("-", 1) == 1
    assert bfs("++", 1) == 0
    assert bfs("+-", 1) == 1
    assert bfs("+-", 2) == -1
    assert bfs("---+-++-", 3) == 3
    assert bfs("+++++", 4) == 0
    assert bfs("-+-+-", 4) == -1

if __name__ == "__main__":
    tests()
    with open(sys.argv[1]) as input:
        lines = input.readlines()
    lines = lines[1:]
    for nr, line in enumerate(lines):
        state, K = line.split(" ")
        K = int(K)
        result = bfs(state, K)
        print "Case #{}: {}".format(nr + 1, result if result >= 0 else "IMPOSSIBLE")