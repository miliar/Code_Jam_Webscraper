from queue import Queue


def neigbours(S, k):
    l = len(S)
    ret = list(S)
    for i in range(l):
        if i + k > l:
            break
        if i == 0:
            for j in range(k):
                ret[j] ^= True
        else:
            ret[i - 1] ^= True
            ret[i + k - 1] ^= True
        yield tuple(ret)


def is_done(S):
    return all(S)


def solution(S, k):
    tracker = {tuple(S): 0}
    queue = Queue()
    queue.put(tuple(S))
    current = S
    goal = (True for _ in S)
    while not queue.empty():
        current = queue.get()
        depth = tracker[tuple(current)]
        if is_done(current):
            return depth
        for neigbour in neigbours(current, k):
            if neigbour not in tracker:
                tracker[neigbour] = depth + 1
                queue.put(neigbour)

    return "IMPOSSIBLE"


if __name__ == '__main__':
    with open("input.txt") as fp:
        lines = fp.readlines()

    T = int(lines[0])
    for i in range(T):
        S, k = lines[1 + i].split()
        print("Case #%d: %s" % (i + 1, solution([s == "+" for s in S], int(k))))
