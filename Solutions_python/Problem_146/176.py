# Written for Python 2.7.5

from optparse import OptionParser
from StringIO import StringIO
from math import factorial
import re
import sys

# Expected format of TEST_CASES is a list of tuples of (input, expected_output)
TEST_CASES = [("""4
3
ab bbbc cd
4
aa aa bc c
2
abc bcd
7
yyyyyy rrrrrrrbbbbbbbbiiiiiiiiiiiccccccchhhhhhhhhnnnnnnnllllleeeeeeeeejjjjjjjjwwwwwwwaaaaaaaaaa yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy ppppppttttttxxxxkkqqqdddmmmmmmoooovvvvvvsssssggguuuuuuuu yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
""","""Case #1: 1
Case #2: 4
Case #3: 0
Case #4: 576
""")]

def parse_input(input_reader):
    case_count = int(input_reader.readline())
    case_idx = 0
    while case_count > case_idx:
        case_idx += 1
        car_count = int(input_reader.readline())
        cars = input_reader.readline().rstrip("\n").split(" ")
        input_values = {"case": case_idx,
                        "cars": cars,
                        "car_count": car_count
                       }
        yield input_values

BAD_STRING = re.compile(r"(.)\1*(?!\1)(.*)(\1)")

def solve_problem(output_writer=sys.stdout, **kwargs):
    case = kwargs['case']
    cars = kwargs['cars']
    car_count = kwargs['car_count']
    starts = {}
    ends = {}
    completes = {}
    idx = 0
    answer = 0
    for car in cars:
        idx += 1
        if BAD_STRING.search(car):
            break
        no_match = False
        for next_car in cars[idx:]:
            if BAD_STRING.search("".join([car,next_car])) and \
               BAD_STRING.search("".join([next_car,car])):
                no_match = True
                break
        if no_match:
            break
        if car[0] == car[-1]:
            completes[car[0]] = completes.get(car[0], 0) + 1
        else:
            if car[0] in starts:
                break
            starts[car[0]] = 1
            if car[-1] in ends:
                break
            ends[car[-1]] = 1
    else:
        multiplier = 1
        unordered_cars = 0
        for letter, count in completes.items():
            if letter not in starts and letter not in ends:
                unordered_cars += 1
            multiplier *= factorial(count)
        for letter, count in starts.items():
            if letter not in ends:
                unordered_cars += 1
        answer = (multiplier * factorial(unordered_cars)) % 1000000007
    print >>output_writer, "Case #%d: %s" % (case, answer)

def solve_inputs(input_reader, output_writer):
    """
    Loop through each problem input in input reader and solve it.

    Outputs responses to output_writer.
    """
    for input_values in parse_input(input_reader):
        solve_problem(output_writer=output_writer, **input_values)

def run_tests():
    idx = 0
    all_pass = True
    for problem_input, expected_output in TEST_CASES:
        idx += 1
        input_reader = StringIO(problem_input)
        output_writer = StringIO()
        solve_inputs(input_reader, output_writer)
        problem_output = output_writer.getvalue()
        if problem_output == expected_output:
            print "Test %d: Success" % idx
        else:
            all_pass = False
            print "Test %d: Failure" % idx
        input_reader.close()
        output_writer.close()
    if all_pass:
        print "All tests were successful!"
    else:
        print "Something didn't match - try again."

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file",
                      dest="filename_stem",
                      help="read input from FILE.in and write to FILE.out",
                      metavar="FILE")

    (options, args) = parser.parse_args()
    if options.filename_stem:
        print "Running in file mode."
        input_reader = open("%s.in" % options.filename_stem, "r")
        output_writer = open("%s.out" % options.filename_stem, "w")
        solve_inputs(input_reader, output_writer)
    else:
        print "Running in test mode."
        run_tests()

if __name__ == "__main__":
    main()