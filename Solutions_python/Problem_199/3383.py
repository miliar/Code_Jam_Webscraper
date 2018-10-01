
def check_plus(s):
    for i in s:
        if i == '-':
            return False
    return True


def flip(flip_str):
    ret_str = ''
    for f in flip_str:
        ret_str += '-' if f == '+' else '+'
    return ret_str


def solve(S, K):
    already_list = []
    length = len(S)
    count = 0
    cakeSide = S

    while(True):
        start_idx = -1
        if cakeSide in already_list:
            return "IMPOSSIBLE"

        for i, s in enumerate(cakeSide):
            if s == '-':
                start_idx = i
                break

        # print(start_idx)
        if start_idx < 0:
            return 0

        if start_idx + K <= length:
            already_list.append(cakeSide)
            result_str = cakeSide[:i] + flip(cakeSide[i:i+K]) + cakeSide[i+K:]
            count += 1
            if check_plus(result_str):
                return count

            cakeSide = result_str
        else:
            return "IMPOSSIBLE"


t = int(input())
for i in range(1, t + 1):
    S, K = (s for s in input().split(" "))
    n = solve(S, int(K))
    print("Case #{}: {}".format(i, n))

