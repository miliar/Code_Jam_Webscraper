f = open('input.txt', 'r')
set1 = []
set2 = []

T = int(f.readline())
for i in range(T):
    row_num1 = int(f.readline())
    for row in range(1, 5):
        if row_num1 == row:
            set1 = f.readline().split()
        else:
            f.readline()

    row_num2 = int(f.readline())
    for row in range(1, 5):
        if row_num2 == row:
            set2 = f.readline().split()
        else:
            f.readline()
    intersect = set(set1).intersection(set(set2))
    message = ""
    if(len(intersect) == 1):
        message = intersect.pop()
    elif(len(intersect) == 0):
        message = "Volunteer cheated!"
    else:
        message = "Bad magician!"
    print("Case #{}: {}".format(i+1, message))

