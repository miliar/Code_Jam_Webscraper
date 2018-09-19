# google codejam qualifier
# problem C
import sys
from case_io import CaseIO
from math import ceil, floor, sqrt

OUT_FILE = "qualifier-C.out"

def is_palindrome(number):
    text = str(number)
    while len(text) > 1:
        if text[0] != text[-1]:
            return False
        text = text[1:-1]
    return True

def root_range(min, max):
    min = sqrt(int(min))
    max = sqrt(int(max))
    return ceil(min), floor(max)
    
if __name__ == "__main__":
    io = CaseIO(sys.argv[1], OUT_FILE, 1, False)
    for case in io.cases():
        min, max = case[0].split()
        min, max = root_range(min, max)
        fair_squares = sum((1 for x in range(min, max+1) if is_palindrome(x) and is_palindrome(x**2)))
        io.write(fair_squares)