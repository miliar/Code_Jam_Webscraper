
with open("magic_trick_input.txt") as f:
    input = f.readlines()

test_cases = int(input[0])
cases = [[] for x in range(test_cases)]
for i in range(test_cases):
    case_array = []
    for j in range(i*9+i+1, i*9+i+10+1):
        case_array.append(input[j].rstrip("\n"))
    cases[i] = case_array

for i, case in enumerate(cases):
    first_row = int(case[0])
    set_1 = set(case[first_row].split(" "))
    second_row = int(case[5]) + 5
    set_2 = set(case[second_row].split(" "))
    result = set_1.intersection(set_2)
    if len(result) == 1:
        print("Case #" + str(i+1) + ": " + str(list(result)[0]))
    elif len(result) > 1:
        print("Case #" + str(i+1) + ": " + "Bad magician!")
    else:
        print("Case #" + str(i+1) + ": " + "Volunteer cheated!")
        
