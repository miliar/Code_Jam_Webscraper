T = int(input())
for tid in range(T):
    N = input()
    A = []
    change = -1
    for x in N:
        A.append(int(x))
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            change = i
            break
    if change == -1:
        print('Case #{}: {}'.format(tid + 1, str(N)))
    else:
        change2 = change
        for i in range(change, -1, -1):
            if A[i] == A[change]:
                change2 = i
        A[change2] -= 1
        for i in range(change2+1, len(A)):
            A[i] = 9
        if A[0] == 0:
            A = A[1:]
        print('Case #{}: {}'.format(tid + 1, ''.join(str(x) for x in A)))
