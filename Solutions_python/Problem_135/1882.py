
def magic_trick(board1, board2, row1, row2):
    a = set(board1[row1])
    b = set(board2[row2])
    intersection = a.intersection(b)
    #print('a: {}'.format(a))
    #print('b: {}'.format(b))
    #print('intersection {}'.format(intersection))
    if not intersection:
        return 'Volunteer cheated!'
    if len(intersection) > 1:
        return 'Bad magician!'
    else:
        return list(intersection)[0]
def main():
    t = int(raw_input())
    for case in range(1, t+1):
        t = t - 1
        row1 = int(raw_input())
        board1 = []
        for _ in range(4):
            board1.append([int(x) for x in raw_input().split()])

        row2 = int(raw_input())
        board2 = []
        for _ in range(4):
            board2.append([int(x) for x in raw_input().split()])

        print('Case #{}: {}'.format(case, magic_trick(board1, board2, row1-1, row2-1)))
        
if __name__ == '__main__':
    main()
