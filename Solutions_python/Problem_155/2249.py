#!/usr/bin/env python3

def people_required(current_people):
    current_standing = 0
    required = 0
    for s_i, num in enumerate(int(i) for i in current_people):
        if current_standing < s_i and num!=0:
            required += s_i - current_standing
            current_standing += s_i - current_standing
        current_standing += num
    return required

def parse_input(input_file):
    input_lines = []
    input_file_object = open(input_file)
    input_file_object.readline()
    for line in input_file_object:
        num_string = line.strip().split()[1]
        input_lines.append(num_string)
    return input_lines

def main(input_file):
    input_lines = parse_input(input_file)
    for index,i in enumerate(input_lines):
        print("Case #{0}: {1}".format(index+1, people_required(i)))

if __name__=="__main__":
    from sys import argv
    main(argv[-1])
