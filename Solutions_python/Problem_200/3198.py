import sys
import math as m

def answer(number, answer):
    print("Case #" + str(number) + ": " + str(answer))

def is_tidy(number):
    s = str(number)
    last_digit = int(s[0])
    for digit in s[1:]:
        if int(digit) < last_digit:
            return False
        last_digit = int(digit)
    return True

#actually returns 1 less than the number of digits 
def length(number):
    return len(str(number))-1

#indexed from zero
def nth_digit(n, number):
    return int(((number%(10**(n+1))) - (number%(10**n)))/10**n)

def max_tidy_below(number):
#    print('ranging from 1 to', length(number)+1, 'with number', number)
    for step in range(1, length(number)+1):
        #print('checking whether', number % (10**(step+1)), 'is tidy')
        if is_tidy(number % (10**(step+1))):
            continue
        else:
            #print("before subtracting", number)
            number = number - (1 + (number % (10**step)) )
            #print("after subtracting", number)
    return number
    
case_num = 0
for line in sys.stdin:
    if case_num == 0:
        case_num+= 1
        continue
    l = line.strip()
    answer(case_num, max_tidy_below(int(l)))
    case_num+= 1
