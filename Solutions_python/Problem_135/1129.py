input = open("input.txt", "r")

cases = int(input.readline())

for case in range(cases):
    answer_1 = int(input.readline()) - 1
    grid_1 = []
    for row in range(4):
        row = map(int, input.readline().split())
        grid_1.append(row)
    answer_2 = int(input.readline()) - 1
    grid_2 = []
    for row in range(4):
        row = map(int, input.readline().split())
        grid_2.append(row)

    possible_1 = grid_1[answer_1]
    possible_2 = grid_2[answer_2]

    match_count = 0
    for card in possible_1:
        if card in possible_2:
            match_count += 1
            match = str(card)

    if match_count == 0:
        result = "Volunteer cheated!"
    elif match_count == 1:
        result = match
    elif match_count > 1:
        result = "Bad magician!"

    print "Case #%i: %s" % (case+1, result)

input.close()