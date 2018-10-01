


with open('input.dat', 'r') as data:

    for index, line in enumerate(data):
        if index == 0:
            pass

        else:
            line_data = line.split(" ")

            max_shy = line_data[0]
            shy_people = None

            if line_data[1][-1] == "\n":
                shy_people = [int(x) for x in line_data[1][:-1]]
            else:
                shy_people = [int(x) for x in line_data[1]]

            invited = 0
            shy_level = 0

            for num, people in enumerate(shy_people):
                if shy_level >= num:
                    shy_level += people
                elif people:
                    invited += num - shy_level
                    shy_level += invited + people

                #print "Shy Level: {} Index: {} Invited: {}".format(shy_level, num, invited)

            with open('out.dat', 'a') as out:
                info = "Case #{}: {}\n".format(index, invited)
                out.write(info)
                #print info
