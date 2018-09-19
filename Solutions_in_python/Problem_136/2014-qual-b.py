import string

testcase = open('testcase', 'r')
num_cases = int(string.strip(testcase.readline()))

for i in xrange(1, num_cases+1):
    params = string.split(string.strip(testcase.readline()), ' ')
    c = float(params[0])
    f = float(params[1])
    x = float(params[2])
    base_cps = 2.0
    farms = 0
    time = 0.0
    while True:
        current_cps = base_cps + f*farms
        time_to_x = x/current_cps
        time_to_farm = c/current_cps
        time_to_x_with_farm = time_to_farm + x/(current_cps+f)
        if time_to_x_with_farm < time_to_x:
            farms += 1
            time += time_to_farm
        else:
            time += time_to_x
            break
    print "Case #"+str(i)+": "+str(time)
