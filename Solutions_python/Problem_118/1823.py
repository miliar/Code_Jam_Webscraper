import math
import json
import sys

import itertools
range = lambda stop: iter(itertools.count().next, stop)

def get_palindromes_under_limit(upper_limit):
    results = []
    for number in range(upper_limit):
        if is_palindrome(number):
            yield number

def generate_fair_and_squares(upper_limit):
    results = []

    for number in get_palindromes_under_limit(int(math.sqrt(upper_limit))):
        square = number * number
        if is_palindrome(square):
            results.append(square)

    print json.dumps(results)

#####

def is_palindrome(number):
    string = str(number)
    counter = len(string) - 1
    for char in string:
        if char != string[counter]:
            return False
        counter -= 1
    return True


########

def get_fair_and_square_numbers(filename):
    with open(filename) as f:
        return json.load(f)

def parse_number_of_test_cases(text):
    number, text = text.split('\n', 1)
    return int(number), text

def parse_text_into_separate_test_cases(text):
    """
    Iterator that outputs one complete test case chunk per

    """    
    for test_case in text.split('\n'):
        yield test_case

def parse_test_case(text):
    lower, upper = text.split()
    return int(lower), int(upper)

def solve(fair_and_square_numbers, lower, upper):
    result = 0
    for number in fair_and_square_numbers:
        if number > upper:
            break
        if number >= lower:
            result += 1
    return result

def print_final_output(output):
    for index, item in enumerate(output):
        print "Case #%s: %s" % (index + 1, item)

def main(filename, text):
    output = []
    fair_and_square_numbers = get_fair_and_square_numbers(filename)
    number_test_cases, text = parse_number_of_test_cases(text)
    for test_case in parse_text_into_separate_test_cases(text):
        if not test_case:
            continue
        lower, upper = parse_test_case(test_case)
        output.append(solve(fair_and_square_numbers, lower, upper))
    print_final_output(output)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "generate":
        #generate_fair_and_squares(int(sys.argv[2]))
        generate_fair_and_squares(10 ** 100)
    elif len(sys.argv) > 1:
        main(sys.argv[1], sys.stdin.read())
    else:
        print "Invald arguments"
