__author__ = 'prahaladd'

import fileinput
import os

input_lines = []

input_lines_position_map = {}

first_question_response_index = 1
second_question_response_index = 6

first_grid_arrangement_start_index = 2
first_grid_arrangement_end_index = 5

second_grid_arrangement_start_index = 7
second_grid_arrangement_end_index = 10

index_increment = 10

def read_input(filename = None):
    global input_lines
    if filename is None:
        for line in fileinput.input():
            input_lines.append(line)
    else:
        for line in fileinput.input(filename):
            input_lines.append(line)
    global input_lines_position_map
    input_lines_position_map = {index : value.strip()  for (index, value) in enumerate(input_lines) if(len(value.strip()) != 0)}


def identify_card(first_row_response, second_row_response):
    global input_lines_position_map
    first_card_set = set(input_lines_position_map[first_row_response].split())
    second_card_set = set(input_lines_position_map[second_row_response].split())
    return first_card_set.intersection(second_card_set)

def print_result(input_chosen_card_set_map):
    for key in input_chosen_card_set_map.keys():
        print 'Case #%s: %s' % (str(key), str(input_chosen_card_set_map[key]))




def main():

    global first_question_response_index
    global second_question_response_index
    global first_grid_arrangement_start_index
    global second_grid_arrangement_start_index

    import sys
    read_input(os.getcwd() + '/' + sys.argv[1])

    num_cases = int(input_lines_position_map[0])

    test_case_output_map = {}

    for i in xrange(num_cases):
        first_response_row = int(input_lines_position_map[(i * index_increment) + first_question_response_index])
        second_response_row = int(input_lines_position_map[(i * index_increment) + second_question_response_index])


        chosen_card_set = identify_card((first_response_row - 1  + (i * index_increment +first_grid_arrangement_start_index)),(second_response_row - 1 + (i * index_increment + second_grid_arrangement_start_index)))
        if(len(chosen_card_set) == 0):
            test_case_output_map[i+1] = 'Volunteer cheated!'
        elif(len(chosen_card_set) > 1):
            test_case_output_map[i+1] = 'Bad magician!'
        else:
            test_case_output_map[i+1] = chosen_card_set.pop()

    print_result(test_case_output_map)


if __name__ == '__main__':
    main()






