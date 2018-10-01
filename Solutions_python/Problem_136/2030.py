f = open('B-large.in')
lines = [i.strip() for i in f.readlines()]
 
number_of_lines = int(lines[0])
for j in range(number_of_lines):
    params = lines[j+1].split(' ')
    C = float(params[0])#500.0
    F = float(params[1])#4.0
    X = float(params[2])#2000.0
    
#     print C,F,X
    min_time = 100000000000
    prev_time = min_time
    total_penalty = 0
    
    for i in range(2000000):
        rate = 2 + (i*F)
        penalty = C/rate
        time = X/rate
        total_time = total_penalty + time
        if total_time < min_time:
            min_time = total_time
        else:
            print "Case #{}: {}".format(j+1,min_time)
            break 
         
    #     print "{:2} {:8.2} {:8.2f} {:8.2f} {:8.2f} {:8.2f}".format(
    #                                                           i,
    #                                                           rate,
    #                                                           time,
    #                                                           penalty,
    #                                                           total_penalty,
    #                                                           total_time
    #                                                           )
        total_penalty = total_penalty + penalty