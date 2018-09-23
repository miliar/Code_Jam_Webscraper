"""
Problem B. Tidy Numbers

Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest,
her pencils are sorted from shortest to longest and her computers from oldest to
newest. One day, when practicing her counting skills, she noticed that some 
integers, when written in base 10 with no leading zeroes, have their digits 
sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 
224488. She decided to call these numbers tidy. Numbers that do not have this 
property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N.
What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. 
Each line describes a test case with a single integer N, the last number counted
by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test
case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ N ≤ 1000.
Large dataset

1 ≤ N ≤ 1018.
Sample


Input 
 	
Output 
 
4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

"""


def get_closest_tidy_number(n):
    if n < 10:
        return n
    n_str = str(n)
    n_len = len(n_str)
    prev_value = -1
    break_idx = -1
    # find position and value of the first digit to the left that breaks
    # non-decreasing order
    for idx in range(len(n_str)):
        value = int(n_str[idx])
        if value < prev_value:
            break_idx = idx
            break
        prev_value = value
    if break_idx == -1:
        return n
    # decimal place from the right: 0 means 1s, 1 means 10s and so on
    # place = len(n_str) - break_idx - 1
    tidy_value = int(n_str[:break_idx] + '0' * (n_len - break_idx)) - 1
    n_str = str(tidy_value)
    while break_idx > 1:
        break_idx -= 1
        if int(n_str[break_idx]) < int(n_str[break_idx - 1]):
            tidy_value = int(n_str[:break_idx] + '0' * (n_len - break_idx)) - 1
            n_str = str(tidy_value)
        else:
            return tidy_value
    return tidy_value


test_cases = int(input())
for i in range(1, test_cases + 1):
    input_str = int(input())
    tidy_number = get_closest_tidy_number(input_str)
    print("Case #{}: {}".format(i, tidy_number))
