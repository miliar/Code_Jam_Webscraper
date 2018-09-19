for n in range(int(input())):
    X, R, C = map(int, input().split())
    repl = True
    if (X>= 7):
        repl = False
    elif ((X >R) and (X > C)):
        replpl =False
    elif ((R * C % X) != 0):
        repl = False
    elif (((X + 1) // 2) > min(R, C)):
        repl= False
    elif X in (1, 2, 3):
        repl= True
    elif (X == 4):
        repl = min(R, C) > 2
    elif (X == 5):
        repl = not(min(R, C) == 3 and max(R, C) == 5)
    elif (X == 6):
        repl = min(R, C) > 3
    print('Case #%d:' % (n + 1), 'GABRIEL' if repl else 'RICHARD')
