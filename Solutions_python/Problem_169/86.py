import sys

T = int(sys.stdin.readline().strip())

def solve(V, X, inputs):
    if len(inputs) > 2:
        return "???"

    if len(inputs) == 1:
        if inputs[0][1] != X:
            return "IMPOSSIBLE"
        else:
            return V / inputs[0][0]

    inputs.sort(key=lambda x: x[1])
    if X < inputs[0][1] or X > inputs[1][1]:
        return "IMPOSSIBLE"

    x1 = inputs[0][1]
    r1 = inputs[0][0]
    x2 = inputs[1][1]
    r2 = inputs[1][0]

    if x1 == x2:
        return V/(r1+r2)

    v1 = V * (X - x2) / (x1 - x2)
    v2 = V - v1

    return max(v1/r1, v2/r2)

for t in range(T):
    N, V, X = [float(_) for _ in sys.stdin.readline().strip().split()]
    N = int(N)

    inputs = []
    for n in range(N):
        ri, xi = [float(_) for _ in sys.stdin.readline().strip().split()]
        inputs.append((ri, xi))

    r = solve(V, X, inputs)
    print("Case #{}: {}".format(t+1, r))

