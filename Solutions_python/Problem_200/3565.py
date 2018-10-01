# Author: Hurturk Yagmur
# Codejam Qualification Round 2017 - Problem B - Tidy Numbers 

import re

def print_case(n, result):
    print("Case #%d: %s" % ((n+1), str(result)))

T = int(raw_input())

def check_number(n):
    max_n = 0
    for ch in str(n):
        if int(ch) > max_n:
            max_n = int(ch)
        elif int(ch) < max_n:
            return False
    return True

for case in range(0, T):
    current = int(raw_input())
    while current > 1 and not check_number(current):
        if "0" in str(current):
            current_str = list(str(current))
            zero_index = str(current).find("0")
            for i, c in enumerate(current_str[zero_index:]):
                current_str[zero_index+i] = "0"
            current = int("".join(current_str))

        current -= 1
            
    print_case(case, current) 
