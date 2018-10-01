from iopart import read_input, write_output


def main():
    distance = []
    competitors = []
    number_of_cases, raw_data = read_input(name_of_file='A-large.in')
    for case in range(int(number_of_cases)):
        local_competitors = []
        data_to_process = raw_data[0].split(' ')
        distance.append(int(data_to_process[0]))
        number_of_competitors = data_to_process[1]
        raw_data = raw_data[1:]
        for number, element in enumerate(range(int(number_of_competitors))):
            start_point, speed = raw_data[number].split(' ')
            local_competitors.append((float(start_point), float(speed)))
        raw_data = raw_data[int(number_of_competitors):]
        competitors.append(local_competitors)
    data = []
    for number, case in enumerate(distance):
        time_table = []
        horses = competitors[number]
        for horse in horses:
            distance_to_travel = distance[number] - horse[0]
            time_table.append(distance_to_travel / horse[1])
        time_to_travel = max(time_table)
        data.append(float(distance[number]) / time_to_travel)
    print(data)
    write_output(data, 'A-large.out')
    # write_output(data, 'test.out')
if __name__ == '__main__':
    main()
