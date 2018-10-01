#!/usr/bin/env python3

def solve(case_no):
    row_1 = int(input().rstrip()) - 1
    table_1 = [[int(y.rstrip()) for y in input().rstrip().split()] for x in range(4)]
    row_2 = int(input().rstrip()) - 1
    table_2 = [[int(y.rstrip()) for y in input().rstrip().split()] for x in range(4)]

    intersection = set(table_1[row_1]).intersection(table_2[row_2])
    if len(intersection) == 0:
        answer = "Volunteer cheated!"
    elif len(intersection) == 1:
        answer = intersection.pop()
    else:
        answer = "Bad magician!"

    print("Case #{}: {}".format(case_no, answer))

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(1, T+1):
        solve(i)
