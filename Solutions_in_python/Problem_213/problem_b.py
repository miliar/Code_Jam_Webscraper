
def get_minimum_rides(N, C, M, pos2cus, cus2pos):
    minimum_rides = 0
    for c in cus2pos:
        minimum_rides = max(minimum_rides, len(cus2pos[c]))
    seats_below = 0
    for i in range(1, N+1):
        seats_below += len(pos2cus[i])
        required_rides = seats_below / i
        if seats_below % i != 0:
            required_rides += 1
        minimum_rides = max(minimum_rides, required_rides)
    return minimum_rides

def problem_solve(N, C, M, pos2cus, cus2pos):
    minimum_rides = get_minimum_rides(N, C, M, pos2cus, cus2pos)
    minimum_shuffles = 0
    for i in range(1, N+1):
        if len(pos2cus[i]) > minimum_rides:
           minimum_shuffles += len(pos2cus[i]) - minimum_rides
    return minimum_rides, minimum_shuffles

def problem_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    
    for i in range(1, T + 1):
        inputs = f.readline().split()
        N = int(inputs[0])
        C = int(inputs[1])
        M = int(inputs[2])

        pos2cus = {j : [] for j in range(1, N + 1)}
        cus2pos = {j : [] for j in range(1, C + 1)}
        for j in range(1, M + 1):
            inputs = f.readline().split()
            P = int(inputs[0])
            B = int(inputs[1])
            pos2cus[P].append(B)
            cus2pos[B].append(P)

        #print N, C, M
        #print problem_solve(N, C, M, pos2cus, cus2pos)

        sol = problem_solve(N, C, M, pos2cus, cus2pos)
        str_sol = " ".join([str(x) for x in sol])
        output_f.write("Case #" + str(i) + ": " + str_sol + "\n")
    return 1

problem_main("B-large.in", "B-large.out")
