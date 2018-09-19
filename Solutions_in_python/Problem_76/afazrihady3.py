#!/usr/bin/env python
"""
2
5
1 2 3 4 5
3
3 5 6

Case #1: NO
Case #2: 11


   0 : 0
   1 : 1
  10 : 2
  11 : 3
 100 : 4
 101 : 5
 110 : 6
 111 : 7
1000 : 8
1001 : 9
1010 : 10
1011 : 11
1100 : 12
1101 : 13
1110 : 14
1111 : 15

xor friendly: 
1, 2, 4, 8, 16
Unfortunately, Patrick is very young and doesn't know how to add properly. He almost knows how to add numbers in binary; but when he adds two 1s together, he always forgets to carry the remainder to the next bit. For example, if he wants to sum 12 (1100 in binary) and 5 (101 in binary), he will add the two rightmost bits correctly, but in the third bit he will forget to carry the remainder to the next bit:

  1100
+ 0101
------
  1001
So after adding the last bit without the carry from the third bit, the final result is 9 (1001 in binary). Here are some other examples of Patrick's math skills:

5 + 4 = 1
7 + 9 = 14
50 + 10 = 56


"""
import sys
import re

class TestCase:
    n_candies_pattern = re.compile(r'^(\d+)')
    candy_values_pattern = re.compile(r'^\s*(\d+)(.*)$')

    def __init__(self, case_number, input_line1, input_line2):
        match = TestCase.n_candies_pattern.match(input_line1)
        n_candies = int(match.group(1))
        candy_values = []
        for i in range(n_candies):
            match = TestCase.candy_values_pattern.match(input_line2)
            candy_values.append(int(match.group(1)))
            input_line2 = match.group(2)
        candy_values.sort()

        result = 'NO'
        patricks = candy_values[:1]
        seans = candy_values[1:]
        while len(seans) > 0:
            if (reduce(lambda x, y: x^y, patricks) == reduce(lambda x, y: x^y, seans)):
                result = sum(seans)
                break
            patricks.append(seans.pop(0))
        
        print('Case #' + str(case_number) + ': ' + str(result))

if len(sys.argv) < 2:
    print('Please specify input file')
    exit()

try:
    f = open(sys.argv[1])
except:
    print('Failed to open input file')
    exit()

n_test_cases = int(f.readline())
for i in range(n_test_cases):
    TestCase(i+1, f.readline(), f.readline())

f.close()
