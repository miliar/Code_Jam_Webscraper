T = int(input())

def solve(case):
    row1 = int(input())
    square1 = [[int(x) for x in input().split()] for i in range(4)]
    row2 = int(input())
    square2 = [[int(x) for x in input().split()] for i in range(4)]
    row1Set, row2Set = set(square1[row1-1]), set(square2[row2-1])
    cap = row1Set.intersection(row2Set)
    print("Case #{}:".format(case), end=" ")
    if len(cap) == 0:
        print("Volunteer cheated!")
    elif len(cap) == 1:
        print(list(cap)[0])
    else:
        print("Bad magician!")

for t in range(T):
    solve(t+1)
