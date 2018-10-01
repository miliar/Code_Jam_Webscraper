
T = int(input())

for case in range(1,T+1):
    (N,K) = map(int, input().split())
    l = K % 2**N == 2**N - 1
    print('Case #%s: %s' % (case, 'ON' if l else 'OFF'))
