t, T = 0, int(input())
while t != T:
    t += 1

    R1, A1 = int(input())-1, [tuple(map(int, input().split())) for i in range(4)]
    R2, A2 = int(input())-1, [tuple(map(int, input().split())) for i in range(4)]

    r = set(A1[R1]).intersection(A2[R2])
    if len(r) > 1:
        out = 'Bad magician!'
    elif len(r) == 1:
        out = r.pop()
    else:
        out = 'Volunteer cheated!'

    print('Case #%d:' % t, out)
    
