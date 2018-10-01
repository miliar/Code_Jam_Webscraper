__author__ = 'vaibhav'


def find_farm_time(farm_val, production, current):
    return (farm_val-current) / production

def current_win_time(production, cookies, to_win):
    return (to_win - cookies) / production

f = open('B-small-attempt0.in')
f1 = open('output2.txt', 'w')

no_of_cases = int(f.readline())

for i in range(0, no_of_cases):
    answer = 0
    current_cookies = 0
    current_production = 2
    values = f.readline()
    values = list(map(float, values.strip().split(' ')))
    farm_cost = values[0]
    farm_production = values[1]
    cookies_to_win = values[2]

    while((cookies_to_win - current_cookies) / current_production >
            find_farm_time(farm_cost, current_production, current_cookies)
            + cookies_to_win / (current_production + farm_production)):

        answer = answer + find_farm_time(farm_cost, current_production, current_cookies)
        current_production += farm_production

    answer += (cookies_to_win - current_cookies) / current_production
    #print "{0:.7f}".format(answer + (cookies_to_win - current_cookies) / current_production)
    answer = "{0:.7f}".format(answer)
    string = 'Case #%d: %s' % (i+1, answer)
    print string
    f1.write(string + '\n')

f.close()
f1.close()