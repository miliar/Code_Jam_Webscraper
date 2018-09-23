import os
from sys import argv
from sys import exit

class Pancake(object):

    def __init__(self, params):
        params_array = params.split()
        self.cases = int(params_array[0])
        self.trials = params_array[1:]
        self.answer = []
        self.og_pancakes = False

    def run(self):
        attempt = 1
        place = 0
        while attempt <= self.cases:
            stalls = int(self.trials[place])
            users = int(self.trials[place+1])
            print 'stals', stalls, 'users:', users
            answer = self.get_answer(stalls, users)
            print answer
            self.append_answer(answer, attempt)
            attempt += 1
            place+= 2


    def get_answer(self, stalls, users, attempt=0):
        #print untidy_number
        middle_stalls = 'O' * stalls
        print middle_stalls
        actual_stalls = '.{0}.'.format(middle_stalls)
        print 'act stalls', actual_stalls
        user = 0
        while  user < users:
            user += 1
            ohs = self.get_groups_of_ohs(actual_stalls)
            print 'ohs',ohs
            largest_oh = max([oh.values() for oh in ohs][0])
            print largest_oh
            key = [oh.keys()[0] for oh in ohs if oh.values()[0] == largest_oh][0]
            print 'key', key
            if largest_oh == 2:
                place = 1
            if largest_oh == 1:
                place = 0
            # if even
            if largest_oh % 2 == 0:
                place = largest_oh / 2 - 1
            else:
                place = (largest_oh - 1) / 2
            print 'key+places', key + place
            actual_stalls = self.mark(key + place, actual_stalls)
        return self.get_empty_stalls_between_place(key + place, actual_stalls)


    def get_empty_stalls_between_place(self, key, actual_stalls):
        stalls_list = [stall for stall in actual_stalls]
        l = 0
        r = 0
        start = 1
        while True:
            if stalls_list[key + start] == 'O':
                r += 1
                start += 1
            else:
                break
        start = 1
        while True:
            if stalls_list[key - start] == 'O':
                l += 1
                start += 1
            else:
                break

        print 'l, r:',l, r
        return [max(l, r), min(l, r)]

    def mark(self, place, actual_stalls):
        stalls_list = [stall for stall in actual_stalls]
        stalls_list[place] = '.'
        print  ''.join(stalls_list)
        return ''.join(stalls_list)
        print 'stallslist', stalls_list





    def get_groups_of_ohs(self, stalls):
        stalls_list = [stall for stall in stalls]
        start = 1
        stalls_len = len(stalls_list)
        groups = []
        while start < stalls_len - 1:
            if stalls_list[start] == 'O':
                current_key = start
                group = {current_key: 0}
                while True:
                    if start < stalls_len - 1 and stalls_list[current_key+1] == 'O':
                        print group
                        group[current_key] += 1
                        start += 1
                    else:
                        groups.append(group)
                        break
            start += 1
        return groups



    def tidy_up(self, number):
        number_str = str(number)
        last_key = len(number_str) - 1
        while last_key > 0:
            last = number_str[last_key]
            second_to_last = number_str[last_key - 1]
            #print second_to_last, last
            if last < second_to_last:
                last = '9'
                second_to_last = str(int(second_to_last) - 1)
            #print second_to_last, last, number_str
            new_str = [trial_char for trial_char in number_str]
            new_str[last_key] = last
            new_str[last_key - 1] = second_to_last
            #print new_str
            number_str = ''.join(new_str)
            #print int(number_str)
            last_key -= 1
        return int(number_str)

    def is_tidy_number(self, number):
        number_str = str(number)
        return all(number_str[i] <= number_str[i+1] for i in xrange(len(number_str)-1))


    def append_answer(self, answer, attempt):
        self.answer.append('Case #{0}: {1} {2}'.format(attempt, answer[0], answer[1]))

    def get_result(self):
        return '\n'.join(self.answer)

def main(file_name):
    with open(file_name, 'r') as inputs:
        google_input = inputs.read()
    pancake = Pancake(google_input)
    pancake.run()
    answer = pancake.get_result()
    with open('answer.txt', 'wr') as answer_file:
        answer_file.write(answer)


if __name__ == '__main__':
    file_name = argv[1]
    main(file_name)


