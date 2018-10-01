import fileinput
file = fileinput.input()
num_case = int(file.readline())
for ith_case in range(num_case):
    first = int(file.readline().strip())
    board = []
    for _ in range(4):
        board.append(list(map(int, file.readline().strip().split())))
    row1 = board[first-1]
    second = int(file.readline().strip())
    board = []
    for _ in range(4):
        board.append(list(map(int, file.readline().strip().split())))
    row2 = board[second-1]
    answer = set(row1) & set(row2)

    output = None
    if len(answer) > 1:
        output = 'Bad magician!'
    elif len(answer) < 1:
        output = 'Volunteer cheated!'
    else:
        output = list(answer)[0]

    print("Case #{}: {}".format(ith_case+1,output))
