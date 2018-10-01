n = int(raw_input())
for it in range(n):
    c = int(raw_input())
    for i in range(1, 5):
        if i == c:
            a1 = (map(lambda x: int(x), raw_input().split(' ')))
        else:
            raw_input()
    c = int(raw_input())
    for i in range(1, 5):
        if i == c:
            a2 = (map(lambda x: int(x), raw_input().split(' ')))
        else:
            raw_input()
    last = 0
    solved = True
    for i in a1:
        if i in a2:
            if last != 0:
                solved = False
            else:
                last = i

    if solved:
        if last == 0:
            ans = 'Volunteer cheated!'
        else:
            ans = last
    else:
        ans = 'Bad magician!'
    print 'Case #' + str(it+1) + ': ' + str(ans)
