import math

# the main function that outputs to a file
def c(filename):
    fd = open(filename, 'rU')
    fd.readline()
    out = []
    for i, s in enumerate(fd):
        lower, upper = [int(j) for j in s.split(' ')]
        result = count_fair_square(lower, upper)
        out.append('Case #{0}: {1}'.format(i+1, result))
    #read the file here
    fd.close()

    #write to the output file
    fd = open('output.txt', 'w')
    for s in out:
        fd.write(s+'\n')
    fd.close()

# the subfunctions that do most of the computation

def count_fair_square(lower, upper):
    sqrt_lower = int(math.ceil(lower**0.5))
    sqrt_upper = int(upper**0.5)
    
    p = starting_palindrome(sqrt_lower)
    out = 0
    while p <= sqrt_upper:
        if is_palindrome(p**2):
            out += 1
        p = next_palindrome(p)

    return out

def is_palindrome(x):
    """Checks if x is a palindrome

    is_palindrome(int) -> bool

    """
    str_x = str(x)
    if str_x == str_x[-1::-1]:
        return True
    else:
        return False

def starting_palindrome(x):
    """Finds the starting palindrome greater than x

    starting_palindrome(int) -> int

    """
    str_x = str(x)
    num_digits = len(str_x)
    if num_digits == 1:
        return x
    else:
        last_half_start = (num_digits+1)/2
        last_half = str_x[last_half_start:]
        first_half_end = num_digits/2-1
        guess = str_x[first_half_end::-1]
        if guess == last_half:
            return x
        elif guess > last_half:
            return int(str_x[:last_half_start]+guess)
        else:
            first_half = str(int(str_x[:last_half_start])+1)
            return int(first_half + first_half[first_half_end::-1])

def next_palindrome(p):
    """Finds the next largest palindrome given a palindrome

    next_palindrome(int) -> int
    Precondition: p is a palindrome

    """
    str_p = str(p)
    num_digits = len(str_p)
    if num_digits == 1 and p < 9:
        return p+1
    elif p == 9:
        return 11
    else:
        first_half = str(int(str_p[:(num_digits+1)/2])+1)
        return int(first_half + first_half[num_digits/2-1::-1])        
