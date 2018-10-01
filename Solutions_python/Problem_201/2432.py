def index_max(ls):
    return ls.index(max(ls))

def solve(n, k):
    stack = []
    el = ((n - 1) // 2, (n - 1) // 2)
    if n % 2 == 0:
        el = (n // 2, n // 2 - 1)
    stack.append(el[0])
    stack.append(el[1])
    
    for i in range(1, k):
        r = stack.pop(index_max(stack))
        if r % 2 == 0:
            el = (r // 2, r // 2 - 1)
        else:
            el = ((r - 1) // 2, (r - 1) // 2)
        stack.append(el[0])
        stack.append(el[1])
    return el


T  = int(input().strip())
for i in range(T):
    n, k = [int(z) for z in input().strip().split(" ")]
    sol1, sol2 = solve(n, k)

    print("Case #" + str(i + 1) + ":", sol1, sol2)

