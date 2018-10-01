import numpy as np
filename = 'B-large'
infile = open('{}.in'.format(filename), 'r')
outfile = open('{}.out'.format(filename), 'w')

base_cps = 2.0

T = int(infile.readline())
for case in range(1, T+1):
    C, F, X = np.array(infile.readline().split()).astype(float)
    cps = base_cps
    total_time = 0

    while True:

        time_to_x = X/cps
        time_to_farm = C/cps
        time_to_x_with_farm = X/(cps + F) + time_to_farm
        if time_to_x_with_farm < time_to_x:
            cps += F
            total_time += time_to_farm
        else: 
            total_time += time_to_x
            break
    print total_time
    outfile.write('Case #{}: {}\n'.format(case, total_time))

infile.close()
outfile.close()

