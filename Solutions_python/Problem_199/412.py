def solve(S, K):
    bits = [1 if c == '+' else 0 for c in S]
    left, right = 0, len(bits) - 1
    count = 0
    while left + K - 1 <= right:
        if bits[left] == 0:
            count += 1
            for k in range(K):
                bits[left + k] = 1 - bits[left + k]
            left += 1
        elif bits[right] == 0:
            count += 1
            for k in range(K):
                bits[right - k] = 1 - bits[right - k]
            right -= 1
        else:
            left += 1
    if all(bits):
        return count
    return 'IMPOSSIBLE'


T = int(input())
for tc in range(T):
    S, K = input().split()
    K = int(K)
    print('Case #{}: {}'.format(tc + 1, solve(S, K)))
