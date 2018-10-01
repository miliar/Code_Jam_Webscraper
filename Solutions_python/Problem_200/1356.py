def read_one(stream, type_to_read=int):
    return type_to_read(stream.readline().strip())


def is_tidy(N):
    prev = 0
    N_str = str(N)
    for c in N_str:
        if int(c) < prev:
            return False
        prev = int(c)
    return True


def solve_small(N):
    sol = N
    while not is_tidy(sol):
        sol-=1
    return str(sol)


def solve(N):
    digits = [int(d) for d in str(N)]

    index = len(digits) - 1
    while index > 0:
        if digits[index] < digits[index-1]:
            for j in range(index, len(digits)):
                digits[j] = 9
            digits[index-1] -= 1
        index -= 1

    answer = ''.join([str(d) for d in digits]).lstrip("0")
    return answer


if __name__ == "__main__":
    import sys
    stream = sys.stdin
    T = read_one(stream, int)
    for t in range(T):
        N = read_one(stream, int)
        solution = solve(N)
        print("Case #{id}: {sol}".format(id=t+1, sol=solution))