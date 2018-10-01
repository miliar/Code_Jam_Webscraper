import pdb
import sys

INPUT_FILE = 'a.in'
OUTPUT_FILE = 'a.out'

sys.stdin = open(INPUT_FILE, 'r')
sys.stdout = open(OUTPUT_FILE, 'w')

def solve(test_case):
    args = raw_input().split(' ')

    # max_shyness = int(args[0])
    shy_people = args[1]

    answer = 0
    total_shy_people = 0
    for shyness_level, number_of_shy_people in enumerate(shy_people):
        if total_shy_people < shyness_level:
            answer += (shyness_level - total_shy_people)  # people added at shyness_level - 1
            total_shy_people = shyness_level
        total_shy_people += int(number_of_shy_people)

    print 'Case #%s: %s' % (test_case, answer)


def main():
    test_cases = int(raw_input())
    for test_case in range(1, test_cases+1):
        solve(test_case)

main()
