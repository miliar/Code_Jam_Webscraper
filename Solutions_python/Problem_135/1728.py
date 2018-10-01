fInput = open("input1.txt", "r")
fOutput = open("output1.txt", "w")

number_of_case = int(fInput.readline())
for i in range(0, number_of_case):
    first_chosen_row = int(fInput.readline())
    first_chosen_row_array = []
    for y in range(0, 4):
        line = fInput.readline()
        if y + 1 == first_chosen_row:
            first_chosen_row_array = [int(x) for x in line.split(" ")]
    # On fait la même chose pour le deuxième
    second_chosen_row = int(fInput.readline())
    second_chosen_row_array = []
    for y in range(0, 4):
        line = fInput.readline()
        if y + 1 == second_chosen_row:
            second_chosen_row_array = [int(x) for x in line.split(" ")]
    # On compare les 2
    common_elements = list(set(first_chosen_row_array).intersection(second_chosen_row_array))
    print(first_chosen_row_array)
    print(second_chosen_row_array)
    print(common_elements)
    fOutput.write("Case #" + str(i + 1) + ": ")
    if len(common_elements) == 0:
        fOutput.write("Volunteer cheated!")
    elif len(common_elements) == 1:
        fOutput.write(str(common_elements[0]))
    else:
        fOutput.write("Bad magician!")
    fOutput.write("\n")