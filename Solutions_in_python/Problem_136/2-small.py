# Magic Trick - Short

import math
import time

time_start = time.time()

file_input = open('B-large.in')
file_out = open('output_2_large.txt','w')
file_out.write('')
file_out.close()

Test_Cases = [int(a) for a in file_input.readline().split(' ')][0]

N = 1

while N <= Test_Cases:

    variables = [float(a) for a in file_input.readline().split(' ')]

    C = variables[0] # cost of cookie farm
    F = variables[1] # Cookies per second from farm
    X = variables[2] # Cookies Goal

    No_Farms = 0
    timefarm = 0

    timeA = timefarm + X/(2+timefarm*No_Farms)

    timefarm += C/(2+F*No_Farms)

    No_Farms += 1

    timeB = timefarm + X/(2+F*No_Farms)

    while timeB < timeA:

        timeA = timeB

        timefarm += C/(2+F*No_Farms)
        No_Farms += 1

        timeB = timefarm + X/(2+F*No_Farms)

    file_out = open('output_2_large.txt','a')
    file_out.write('Case #'+str(N)+': '+"{0:.7f}".format(timeA)+'\n')
    file_out.close()

    N+=1

time_end = time.time()

print('Time taken: '+str(time_end-time_start)+' sec')
