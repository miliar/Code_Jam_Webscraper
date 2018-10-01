import math
import sys

def is_palindrome(num):
    string = str(num)
    left = 0;
    right = len(string) - 1;

    while (left < right):
        if (string[left] != string[right]):
            return False
        left+=1
        right-=1
    return True

# make a palindrome by flipping the first half
def make_palin(num_string):
    midpoint = len(num_string)/2
    flip_half = num_string[0:midpoint]
    
    if len(num_string) % 2 == 0: first_half = num_string[0:midpoint] 
    else: first_half = num_string[0:midpoint+1]

    return first_half + flip_half[::-1]

def increment_digit(num_string, index):
    # check for overflow
    if num_string[index] == '9':
        if index == 0: #yes overflow        
            num_string = '10' + num_string[1:]
        else: #no, but carry over, recursively
            num_string = num_string[:index] + '0' + num_string[index+1:]
            num_string = increment_digit(num_string, index - 1)
    else: num_string = num_string[:index] + str(int(num_string[index]) + 1) + num_string[index+1:]
    return num_string

def increment_mid_digit(num_string):
    midpoint = len(num_string)/2
    if(len(num_string) % 2 == 0): return increment_digit(num_string, midpoint-1)
    else: return increment_digit(num_string, midpoint)

def next_palin(number):
    num_string = str(number)
    
    #make a best effort by flipping the first half
    flip_palin = long(make_palin(num_string))

    # if it's greater, we're done
    if flip_palin > number:
        return flip_palin
    # otherwise, we increment the middle digit (and fan out if appropriate) to get to the next palin
    return long(make_palin(increment_mid_digit(num_string)))

def fair_and_square(start,end,debug=False):
    count = 0
    i = long(math.sqrt(start))
    i2 = i**2
    while True:
        if i2 > end: break
        if is_palindrome(i2) and i2 >= start:
            if(debug): print i2
            count +=1
        i = long(next_palin(i))
        i2 = i**2
    return count

if __name__=="__main__":
    cases = sys.stdin.readline()
    try:
        cases = int(cases.strip())
        for case in xrange(1,cases+1):
            input = [long(x.strip()) for x in (sys.stdin.readline()).split(' ')]
            print "Case #%s: %d" % (case, fair_and_square(input[0], input[1]))
    except Exception as e:
        print "something went wrong: %s" % e