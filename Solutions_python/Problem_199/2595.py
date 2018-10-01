def check(S):
    for s in S:
        if s == -1:
            return False
    return True


t = int(input())
for i in range(1, t + 1):
    raw = [str(s) for s in input().split(" ")]
    S = list(raw[0])
    S = [-1 if s == '-' else 1 for s in S]
    K = int(raw[1])

    flip = 0
    index = 0
    for useless_i in range(len(S)):
        if index + K > len(S):
            flip = flip if check(S) else 'IMPOSSIBLE'
            break

        cur = S[index]
        if cur == -1:
            for ii in range(K):
                try:
                    S[index + ii] = -1 * S[index + ii]
                except Exception:
                    pass
            index += 1
            flip += 1
        else:
            index += 1

    print("Case #{}: {}".format(i, flip))
