import sys
T = int(input())
for case in range(1, T+1):
    n, r, o, y, g, b, v = map(int, input().split())
    stable = []
    if r:
        stable.append(0)
        r -= 1
    elif b:
        stable.append(1)
        b -= 1
    elif y:
        stable.append(2)
        y -= 1
    h = [r, b, y]
    for i in range(n-1):
        l = stable[i]
        if h[l-1] > h[l-2] or (h[l-1] == h[l-2] and (l-1) % 3 == stable[0]):
            h[l-1] -= 1
            stable.append((l-1) % 3)
        else:
            h[l-2] -= 1
            stable.append((l-2) % 3)

    if any(h) or stable[0] == stable[-1]:
        print(f"Case #{case}: IMPOSSIBLE")
    else:
        print(f"Case #{case}: ", end="")
        for h in stable:
            print("RBY"[h], end="")
        print()
