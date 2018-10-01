import fileinput

def main():
    input = []
    for line in fileinput.input():
        input.append(line)

    numcases = int(input[0])

    for i in xrange(numcases):
        parameters = [float(num) for num in input[i +1].split()]
        cost, farm_rate, target_num = parameters[0], parameters[1], parameters[2]
        base_rate = 2.0
        t_elapsed = 0.0
        num_cookies = 0.0
        while num_cookies < target_num:
            #print "t,cookies: " + str(t_elapsed) + ", " + str(num_cookies)
            #wait to buy a farm
            #either buy another farm
            #or win
            if num_cookies < cost:
                t = min((cost-num_cookies), (target_num-num_cookies))/base_rate
                num_cookies += t * base_rate
            else:
                t_buy = (target_num - num_cookies + cost) /(base_rate + farm_rate)
                t_wait = (target_num - num_cookies)/(base_rate)
                if t_buy < t_wait:
                    t = 0
                    base_rate += farm_rate
                    num_cookies -= cost
                else:
                    t = t_wait
                    num_cookies += t * base_rate
            t_elapsed += t
        print "Case #" + str(i+1) + ': ' + str(t_elapsed)


if __name__ == '__main__':
    main()
