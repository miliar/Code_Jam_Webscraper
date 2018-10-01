f = open('A-small-attempt0.in', 'r')
o = open('A-small-attempt0.out', 'w')

T = int(f.readline())

for t in range(T):
    ans1 = int(f.readline())
    grid1 = []
    for x in range(4):
        grid1.append(map(int, f.readline().split(' ')))

    ans2 = int(f.readline())
    grid2 = []
    for y in range(4):
        grid2.append(map(int, f.readline().split(' ')))

    row1 = set(grid1[ans1-1])
    row2 = set(grid2[ans2-1])

    intersection = row1 & row2

    if len(intersection) == 1:
        output = str(list(intersection)[0])
    elif len(intersection) == 0:
        output = 'Volunteer cheated!'
    else:
        output = 'Bad magician!'

    o.write("Case #%d: %s\n" %(t+1, output))