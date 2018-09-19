input_file = open('input02.txt', 'r')
output_file = open('output02.txt', 'w')

case_number = int(input_file.readline())

for i in range(case_number):
    game_cps = 2
    factory_price, factory_production, game_finish = [float(j) for j in input_file.readline().split()]
    time_sum = 0
    time_buy = [0]
    time_finish = [game_finish / game_cps]

    best = game_finish / game_cps

    while True:
        time_sum += factory_price / game_cps
        game_cps += factory_production

        if time_sum + (game_finish / game_cps) < best:
            best = time_sum + (game_finish / game_cps)
        else:
            break

    print "%.7f" % best

    output_file.write('Case #' + str(i + 1) + ': ' + "{0:.7f}".format(best) + '\n')
