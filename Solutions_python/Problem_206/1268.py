#problem 1 solution

def get_input():
    input_array = []
    with open("A-large.in", "r") as ins:
        cases = int(ins.readline())
        for case in range(0,cases):
            line = ins.readline().split(" ")
            distance = float(line[0])
            horses = int(line[1])
            horses_data = []
            for horse in range(0, horses):
                line = ins.readline().split(" ")
                horse_at = float(line[0])
                horse_speed = float(line[1])
                horses_data.append({
                    "distance": horse_at,
                    "speed": horse_speed
                })
            input_array.append({
                "total_distance": distance,
                "horses": horses_data
            })
    return input_array

def solve(problem):
    """
    solve a problem set
    """
    total_distance = problem['total_distance']
    horses = problem['horses']
    times = []
    for horse in horses:
        time = (total_distance-horse['distance'])/horse['speed']
        times.append(time)
    print 'minimum is '.format(max(times))
    annie_speed = total_distance/max(times)
    return annie_speed


def solution():
    output_string = """"""
    inputs = get_input()
    # print inputs
    for count, problem in enumerate(inputs):
        output_string+="Case #{}: {}\n".format(count+1, solve(problem))
    # print output_string
    output_file = open('output_problem1.txt', 'w+')
    output_file.write(output_string)


if __name__ == "__main__":
    solution()