T = int(input())

for i in range(T):
    ans1 = int(input())
    grid1 = [list(map(int, input().split())) for i in range(4)]
    ans2 = int(input())
    grid2 = [list(map(int, input().split())) for i in range(4)]
    row1 = grid1[ans1-1]
    row2 = grid2[ans2-1]
    l = [i for i in row1 if i in row2]
    print('Case #%d: ' % (i+1), end='')
    if len(l) == 0:
        print('Volunteer cheated!')
    elif len(l) == 1:
        print(l[0])
    else:
        print('Bad magician!')
