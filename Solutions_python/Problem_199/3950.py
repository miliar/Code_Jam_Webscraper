import sys


def flip(state):
    return "".join(list(map(lambda s: "+" if s == "-" else "-", state)))


def flip_seg(state, i, j):
    head = state[:i]
    body = state[i:j]
    tail = state[j:]

    return head + flip(body) + tail


def all_happy(state):
    for s in state:
        if s == "-":
            return False

    return True


def search(state, k):
    if all_happy(state):
        return 0

    queue = [(state, 1)]
    visited = {state: True}

    while len(queue) > 0:
        s, depth = queue[0]
        queue = queue[1:]

        for i in range(len(s) - k + 1):
            j = i + k

            flipped = flip_seg(s, i, j)

            if all_happy(flipped):
                return depth
            elif flipped not in visited:
                visited[flipped] = True
                queue.append((flipped, depth+1))

    return -1


def solve(data, case_no):
    state, k = data.split(" ")
    k = int(k)

    result = search(state, k)

    if result == -1:
        print("Case #{}: IMPOSSIBLE".format(case_no))
    else:
        print("Case #{}: {}".format(case_no, result))


def main():
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        T = int(f.readline().strip())

        for t in range(T):
            solve(f.readline().strip(), t+1)


if __name__ == '__main__':
    main()
