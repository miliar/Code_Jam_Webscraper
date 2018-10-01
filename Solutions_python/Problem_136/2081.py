with open("B-large.in", "r") as r:
    test_case = 0
    for idx, line in enumerate(r):
        line = line[:-1]
        if idx == 0:
            test_cases = int(line)
            test_case = 0
            if test_cases < 1 or test_cases > 100:
                print "Error: number of test cases invalid!"
                break
        else:
            test_cases -= 1
            if test_cases >= 0:
                test_case += 1
                try:
                    c, f, x = [float(x) for x in line.split(' ')]
                except:
                    print "Error!"
                    break
                secs = 0.0
                rate = 2.0
                while x > 0:
                    if x < c:
                        secs += x/rate
                        x = 0
                    else:
                        if_u_buy = (c/rate)+(x/(rate+f))
                        if_u_tank = x/rate
                        if if_u_buy < if_u_tank:
                            secs += c/rate
                            rate += f
                        else:
                            secs += if_u_tank
                            x = 0
                print "Case #"+str(test_case)+": %.7f" % secs
            else:
                break
