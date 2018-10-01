T = int(input())


def get_largest(x):
    if x == 1:
        return 1, 1
    elif x == 2:
        return 2, 1
    elif x == 3:
        return 2, 2
    elif x == 4:
        return 2, 3


for i in range(1, T+1):
    x, r, c = map(int, input().split(" "))

    total = r * c

    if total % x != 0:
        winner = "RICHARD"
    else:
        max_omino_area = get_largest(x)
        max_height = max_omino_area[0]
        max_width = max_omino_area[1]

        min_area = min(max_height, max_width)
        min_height = min(r, c)

        max_area = max(max_height, max_width)
        max_heigh = max(r, c)

        area = r * c
        max_area_of_omino = max_width*max_height

        if min_area > min_height:
            winner = "RICHARD"
        elif max_area > max_heigh:
            winner = "RICHARD"

        elif min_area == min_height and x > 3:
            winner = "RICHARD"
        else:
            winner = "GABRIEL"


    print("Case #{0}: {1}".format(i, winner))