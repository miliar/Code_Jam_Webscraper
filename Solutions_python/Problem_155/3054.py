
with open("A-large.in") as input_file:
    output_file = open("output.txt", "w")

    skip = input_file.readline().strip()

    for index, line in enumerate(input_file):
        case_info = line.split()
        max_shyness = int(case_info[0])
        friends_needed = 0
        audience = 0
        for min_needed, shyness_count in enumerate(case_info[1]):
            if shyness_count != 0:
                if audience < min_needed:
                    need_to_invite = min_needed - audience
                    friends_needed += need_to_invite
                    audience += need_to_invite
                audience += int(shyness_count)
        output_file.write("Case #{}: {}".format(index+1, friends_needed) + "\n")
