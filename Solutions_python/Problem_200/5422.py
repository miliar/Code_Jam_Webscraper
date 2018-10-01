def is_tidy(num):
    digits = list(str(num))
    for i, digit in enumerate(digits):
        if i+1 != len(digits): 
            if digits[i] > digits[i+1]:
                return False
    return True

def find_last_tidy_num(N):
    while N >= 0:
        if is_tidy(N):
            return N
        N = N-1

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  print "Case #{}: {}".format(i, find_last_tidy_num(int(raw_input().replace(' ', ''))))