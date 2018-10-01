

def foo(S, K):
    # print(S)
    if len(S) == K and all([ch=='+' for ch in S]):
        return 0
    if len(S) < K:
        return "IMPOSSIBLE"
    if S[0] == '+':
        return foo(S[1:], K)
    if S[0] == '-':
        for x in range(K):
            S[x] = '+' if S[x]=='-' else '-'
        r = foo(S, K)
        if r == "IMPOSSIBLE":
            return r
        return foo(S, K) + 1

T = int(input())
for _ in range(T):
    S, K = input().split(" ")
    S = list(S)
    K = int(K)
    # print(foo(S, K))
    print("Case #{}: {}".format(_+1, foo(S, K)))