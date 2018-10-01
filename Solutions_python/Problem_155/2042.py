output = open("output.txt", "w")

line_index = 0
with open("input.txt") as input:
    for line in input.readlines():
        tokens = line.strip().split(' ')
        if line_index != 0:
            needed_count = 0
            stood_up_count = 0
            data = tokens[1]
            index = 0
            for str_number in list(data):
                num = int(str_number)
                if (index >= stood_up_count):
                    if num == 0:
                        needed_count += 1
                        stood_up_count += 1
                    else:
                        needed_count += (index - stood_up_count)
                        stood_up_count += (index - stood_up_count)
                stood_up_count += num
                index += 1
            output.write("Case #" + str(line_index) + ": " + str(needed_count) + "\n")
        line_index += 1

output.close()
