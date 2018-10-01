o = open("q2.output", 'r+')

cnt = 1

with open ("q2.input") as f:
    # read the fistline as the T
    T = f.readline()
    print 'No of test cases:', T,

    while True:
        t_case = f.readline()
        if not t_case:
            print "-- End of file"
            break

        output = 0

        print "test case :", t_case,

        case_list = t_case.split()

        N = case_list[0]
        S = case_list[1]
        p = case_list[2]

        for x in range(3,len(case_list)):
            if float(case_list[x])/3 > int(p)-0.7:
                output += 1
            elif float(case_list[x])/3 > int(p)-1.4 and int(S) > 0 and int(case_list[x]) >= int(p):
                S = int(S) - 1
                output += 1

        o.write('Case #')
        o.write(str(cnt))
        o.write(': ')
        o.write(str(output))
        o.write('\n')
        cnt += 1

o.close()
