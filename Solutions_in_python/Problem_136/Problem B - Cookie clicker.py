#Open input
case_file = open('Sample.txt')
total_cases = int(case_file.readline())
case_string = case_file.read()
lines= case_string.splitlines()




for case in xrange(1, total_cases+1):
    farms = 0
    base_production = 2
    cookies = 0
    vars = [float(var) for var in  lines[case-1].split()]
    c,f,x = vars
    time = 0
    while cookies != x:
        prod = farms * f + base_production
        farm_time = c/prod
        x_time_extra_farm = x/(prod+f) + farm_time
        x_time = x/prod
        if(x_time > x_time_extra_farm):
            time += farm_time
            farms += 1
        else:
            time += x_time
            cookies = x
    print "Case #{0}: {1:.7f}".format(case, time)






