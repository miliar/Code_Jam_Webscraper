def lr(A, i):
    l = r = i
    while A[l] == 0:
        l -= 1
    while A[r] == 0:
        r += 1
    l = i - l - 1
    r = r - i - 1
    return (min(l, r), max(l, r))

def bst(A):
    b = -1
    l = r = -1
    for i in range(1, len(A) - 1):
        if A[i] == 0:
            lx, rx = lr(A, i)
            if b == -1 or (lx > l or (lx == l and rx > r)):
                l, r = lx, rx
                b = i
    return b

def main():
    n, k = map(int, input().split())
    A = [0] * (n + 2)
    A[0] = A[-1] = 1
    for i in range(k - 1):
        A[bst(A)] = 1
    b = bst(A)
    l, r = lr(A, b)
    print(r, l)


T = int(input())
for t in range(1, T + 1):
    print("Case #%d: " % t, end="")
    main()