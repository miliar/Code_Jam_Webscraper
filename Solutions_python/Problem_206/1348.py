def load_data(filename):
    with open(filename) as file_handle:
        content = file_handle.read().splitlines()
    
    num_cases = int(content[0])
    
    retval = []
    line_idx = 1
    for idx in range(1, num_cases + 1):
        sample = content[line_idx]
        dest, num_horses = sample.split(' ', 2)
        horses = []
        for n in range(1, int(num_horses) + 1):
            sample = content[line_idx + n]
            posn, speed = sample.split(' ', 2)
            horses.append((posn, speed))
            
        line_idx += n + 1
        retval.append((dest, horses))
    
    return retval

def calc_arrival(start, dest, speed):
    travel_dist = int(dest) - int(start)
    
    return float(travel_dist) / float(speed)

def main():
    input_file = 'roundB/A-large.in'
    # input_file = 'round2-A-sample.txt'
    ride_list = load_data(input_file)
    idx = 1;
    
    for ride_tuple in ride_list:
        dest = ride_tuple[0]
        time_array = []
        for horse in ride_tuple[1]:
            time = calc_arrival(horse[0], dest, horse[1])
            #print("Time = {}".format(time))
            time_array.append(time)
            
        #print("MAX = {}".format(max(time_array)))
        travel_time = max(time_array)
        speed = float(dest) / travel_time

        print("Case #{}: {:.8f}".format(idx, speed))
        idx += 1


if __name__ == '__main__':
    main()
