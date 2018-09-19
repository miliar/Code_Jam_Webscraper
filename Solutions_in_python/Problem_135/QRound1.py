def run():
    f = open('A-small-attempt0.in')
    number_of_testcase = f.readline()

    for test_case in range(1, int(number_of_testcase)+1):
        game_list = []
        for game in range(10):
            game_list.append(f.readline())

        round1_row = int(game_list[0])
        round2_row = int(game_list[5])

        result_set = set(game_list[0 + round1_row].strip().split(' ')).intersection(game_list[5 + round2_row].strip().split(' '))
        if len(result_set) == 1:
            print '%s%s%s%s' % ('Case #', test_case, ': ', list(result_set)[0])
        elif len(result_set) > 1:
            print '%s%s%s' % ('Case #', test_case, ': Bad magician!')
        else:
            print '%s%s%s' % ('Case #', test_case,': Volunteer cheated!')

    f.close()

if __name__ == '__main__':
    run()