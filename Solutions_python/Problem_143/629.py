def main(t):
    A, B, K = [int(x) for x in raw_input().split()]
    ans = (A+B-K)*K
    for n1 in range(K, A):
        for n2 in range(K, B):
            if (n1 & n2) < K:
                ans += 1
    if A <= K or B <= K:
        ans = A*B
    print 'Case #{}:'.format(t+1),
    print ans


if __name__ == '__main__':
    T = input()
    for t in range(T):
        main(t)
