# GCJ 2014 Qualification Round Problem B
# Cookie Clicker Alpha

#In this problem, you start with 0 cookies. You gain cookies at a rate
#of 2 cookies per second, by clicking on a giant cookie. Any time you
#have at least C cookies, you can buy a cookie farm. Every time you
#buy a cookie farm, it costs you C cookies and gives you an extra F
#cookies per second.

#Once you have X cookies that you haven't spent on farms, you win!
#Figure out how long it will take you to win if you use the best
#possible strategy.

#Input

#The first line of the input gives the number of test cases, T. T
#lines follow. Each line contains three space-separated real-valued
#numbers: C, F and X, whose meanings are described earlier in the
#problem statement.

#C, F and X will each consist of at least 1 digit followed by 1
#decimal point followed by from 1 to 5 digits. There will be no
#leading zeroes.

#Output

#For each test case, output one line containing "Case #x: y", where x
#is the test case number (starting from 1) and y is the minimum number
#of seconds it takes before you can have X delicious cookies.

#We recommend outputting y to 7 decimal places, but it is not
#required. y will be considered correct if it is close enough to the
#correct number: within an absolute or relative error of 10**-6. See the
#FAQ for an explanation of what that means, and what formats of real
#numbers we accept.

#Limits

#1 <= T <= 100

#Small dataset

#1 <= C <= 500
#1 <= F <= 4
#1 <= X <= 2000

#Large dataset

#1 <= C <= 10000
#1 <= F <= 100
#1 <= X <= 100000

#Example

#Suppose C=500.0, F=4.0 and X=2000.0. Here's how the best possible
#strategy plays out:

#1. You start with 0 cookies, but producing 2 cookies per second.

#2. After 250 seconds, you will have C=500 cookies and can buy a farm
#that produces F=4 cookies per second.

#3. After buying the farm, you have 0 cookies, and your total cookie
#production is 6 cookies per second.

#4.The next farm will cost 500 cookies, which you can buy after about
#83.3333333 seconds.

#5.After buying your second farm, you have 0 cookies, and your total
#cookie production is 10 cookies per second.

#6.Another farm will cost 500 cookies, which you can buy after 50 seconds.

#7. After buying your third farm, you have 0 cookies, and your total
#cookie production is 14 cookies per second.

#8. Another farm would cost 500 cookies, but it actually makes sense
#not to buy it: instead you can just wait until you have X=2000
#cookies, which takes about 142.8571429 seconds.

#Total time: 250 + 83.3333333 + 50 + 142.8571429 = 526.1904762 seconds.

#Notice that you get cookies continuously: so 0.1 seconds after the
#game starts you'll have 0.2 cookies, and n seconds after the game
#starts you'll have 2n cookies.

from decimal import *

FILE_NAME = "QR_B_CookieClickerAlpha_large-attempt0.in"
OUTPUT = "QR_B_CookieClickerAlpha_large-attempt0.out"

def load_file():
    '''open text file and insert each line into a list'''
    in_file = open(FILE_NAME, 'r', 0)
    line_list = list(in_file)
    in_file.close()
    # remove all newline chars from the list of strings
    line_list = [i.strip('\n') for i in line_list]
    # convert strings to lists to make list of lists
    line_list = [line_list[i].split() for i in range(len(line_list))]
    # cast all list elements to type int
    line_list = [map(float, line_list[i]) for i in range(len(line_list))]
    return line_list

def min_cookie_time(cookie_data):
    '''
    ListOfFloats -> Float
    [C, F, X] -> y

    Given the floats C (Cost of cookie farm), F (Farm production per
    sec), and X (cookie goal) return the min number of seconds required
    to achieve X

    >>> min_cookie_time([30.0, 1.0, 2.0])
    1.0

    >>> min_cookie_time([30.0, 2.0, 100.0])
    39.1666667

    >>> min_cookie_time([30.50000, 3.14159, 1999.19990])
    63.9680013

    >>> min_cookie_time([500.0, 4.0, 2000.0])
    526.1904762

    >>> min_cookie_time([10.0, 4.0, 1.0])
    0.5
    '''
    ## variable definitions
    C = Decimal(cookie_data[0]) # cost of Cookie farm
    F = Decimal(cookie_data[1]) # Farm's cookie production rate per second
    X = Decimal(cookie_data[2]) # cookie goal: X cookies
    r0 = Decimal(2.0)       # existing cookie production rate
    r1 = Decimal(r0 + F)    # improved production rate if farm is bought
    T_c = Decimal(C/r0)     # Time req'd to earn cookies to buy farm
    T_1 = Decimal(X/r1)     # Time req'd to meet cookie goal at rate r1
    T_0 = Decimal(X/r0)     # Time req'd to meet cookie goal at rate r0
                            #(no new farm)
    T_build = Decimal(T_c + T_1)  # Time to meet ckie goal including farm
                                  # acq. time
    T_tot = Decimal(0.0)

    ## logic for calculating min time required to meet goal X
    while T_build < T_0:
        T_tot += Decimal(T_c)
        r0 += Decimal(F)
        r1 += Decimal(F)
        T_c = Decimal(C/r0)
        T_1 = Decimal(X/r1)
        T_0 = Decimal(X/r0)
        T_build = Decimal(T_c + T_1)
    # once loop condition no longer satisfied, add T_0 to T_tot
    T_tot += Decimal(T_0)
    return round(Decimal(T_tot), 7)

def num_cases(list_file):
    '''
    ListOf Float -> Int
    Given a list sublists containing floats, return an int
    denoting the number of cases to consider.
    **NOTE**: this function mutates the input list!

    >>> num_cases([[2.0], [30.0, 1.0, 2.0], [30.0, 2.0, 100.0]])
    2
    '''
    ncases = list_file.pop(0)[0]
    ncases = int(ncases)
    return ncases

def next_case(list_file):
    '''
    ListOf Float -> ListOf Float
    Given a list of lines containing sublists of ints, return the
    next case where a case is defined as the list of floats:
    [C, F, X]

    **NOTE**: this function mutates the input list!

    >>> next_case([[30.0, 1.0, 2.0], [30.0, 2.0, 100.0], [500.0, 4.0, 2000.0]])
    [30.0, 1.0, 2.0]
   '''
    nextc = list_file.pop(0)
    return nextc

def write_out(outfile):
    '''
    -> File
    Calls helper functions and writes output to outfile
    '''

    output_file = open(outfile, 'w')
    input_list = load_file()
    copy_input = input_list
    ans = 0
    case_cnt = 1

    for i in range(num_cases(copy_input)):
        ans = min_cookie_time(next_case(copy_input))
        output_file.write(
            'Case #' + str(case_cnt) + ': ' + str(ans) + '\n')
        case_cnt += 1
    output_file.close()

## MAIN PROGRAM ##
write_out(OUTPUT)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
