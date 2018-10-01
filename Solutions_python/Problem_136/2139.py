import sys

def main():
    f = None
    output = None
    case = 1
    if len(sys.argv) > 1 :
        f = open(sys.argv[1])
        output = open(sys.argv[1][:-2] + 'out', 'w')
    else:
        print("PROBLEM")
        return
    tests = int(f.readline().strip())
    case = 1
    cost = 0
    goal = 0
    farm = 0
    for t in range(tests):
        output.write("Case #" + str(case) + ": ")
        line = f.readline()
        data = line.strip().split()
        cost = float(data[0])
        farm = float(data[1])
        goal = float(data[2])
        seconds_to_win = min_time(cost, farm, goal)
        output.write("{:.7f}\n".format(seconds_to_win))
        case += 1

    f.close()
    output.close()

def min_time(cost, farm, goal):
    time = 0
    farms = 0
    def time_to_win(num_farms):
        return goal / (2 + farm * num_farms)
    def time_to_buy(num_farms):
        return cost / (2 + farm * num_farms)
    while True:
        if time_to_win(farms) <= time_to_win(farms+1) + time_to_buy(farms):
            return time + time_to_win(farms)
        else:
            time += time_to_buy(farms)
            farms += 1

if len(sys.argv) > 1:
    main()
