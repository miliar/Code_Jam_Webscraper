#GJAM
#inn.in
from sys import * 

def execute():
        input_name = argv[1]
        output_name = "out.txt"
        input_file = open(input_name)
        output_file = open(output_name, 'w')

        main(input_file, output_file)

        input_file.close()
        output_file.close()


def last_tidy(number):
    if number == [0]:
        return [] 
    elif len(number) == 1:
        return number

    # find first clash
    good = True 
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            good = False
            break
    if good:
        return number

    smaller_num = number[:i+1]
    smaller_num[-1] = smaller_num[-1] - 1
    return last_tidy(smaller_num) + [9]* (len(number) - i - 1) 

def main(input_file, output):
        # main algorithm goes here
        T = int(next(input_file))
        for case in range(T):
            number = [int(x) for x in next(input_file).strip()]
            out = ''.join([str(x) for x in last_tidy(number)])
            output.write("Case #%i: %s\n" % (case + 1, out))

execute()
