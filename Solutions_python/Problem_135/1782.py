f = open("A-small-attempt0.in", "r+")
output = open("output.txt", "w")

num_cases = int(f.readline())

for case_num in range(0, num_cases):
    grid_1_correct_row = int(f.readline())

    grid_1 = []
    for i in range(0, 4):
        grid_1.append([int(i) for i in f.readline().split(" ")])

    grid_2_correct_row = int(f.readline())
    
    grid_2 = []
    for i in range(0, 4):
        grid_2.append([int(i) for i in f.readline().split(" ")])

    correct_row_1 = grid_1[grid_1_correct_row - 1]
    correct_row_2 = grid_2[grid_2_correct_row - 1]

    common_items = list(set(correct_row_1) & set(correct_row_2))

    output.write("Case #" + str(case_num + 1) + ": ")
    
    if len(common_items) == 1:
        output.write(str(common_items[0]) + "\n")
    elif len(common_items) > 1:
        output.write("Bad magician!\n")
    elif len(common_items) == 0:
        output.write("Volunteer cheated!\n")

f.close()
output.close()
