def init():
    # ('sign', 'num')
    d = {
        1  : { 1  : ( 1,  1 ),
              'i' : ( 1, 'i'),
              'j' : ( 1, 'j'),
              'k' : ( 1, 'k')},
       'i' : { 1  : ( 1, 'i'),
              'i' : (-1,  1 ),
              'j' : ( 1, 'k'),
              'k' : (-1, 'j')},
       'j' : { 1  : ( 1, 'j'),
              'i' : (-1, 'k'),
              'j' : (-1,  1 ),
              'k' : ( 1, 'i')},
       'k' : { 1  : ( 1, 'k'),
              'i' : ( 1, 'j'),
              'j' : (-1, 'i'),
              'k' : (-1,  1)}
    }
    return d



def divide(l, x, case_string):
    def c_in_string(n):
        return d[1][case_string[n % l]]
    
    def compute(start, end):
        n = start
        total = (1, 1)
        while n < end:
            now = c_in_string(n)

            sign = total[0] * d[total[1]][now[1]][0]
            unsigned_num =  d[total[1]][now[1]][1]
            total = (sign, unsigned_num)

            n += 1

        return total

    if compute(0, l*x) != (-1, 1):
        return False
    
    for second_start in xrange(1, l*x-1):
        if compute(0, second_start) == (1, 'i'):
            print "found i @", second_start-1

            if compute(second_start, l*x) != (1, 'i'):
                return False
            
            for third_start in xrange(second_start+1, l*x):
                second = compute(second_start, third_start)
                if second == (1, 'j'):
                    print "found j @", third_start-1
                    third = compute(third_start, l*x)
                    if third == (1, 'k'):
                        print "found k @ end"
                        return True
    return False
                    


def solve(l, x, case_string):
    result = False
    #print l, x, case_string

    if l * x < 3:
        result = False
    # only 'i'
    elif ('j' not in case_string) and ('k' not in case_string):
        result = False
    # only 'j'
    elif ('i' not in case_string) and ('k' not in case_string):
        result = False
    # only 'k'
    elif ('i' not in case_string) and ('j' not in case_string):
        result = False
    elif divide(l, x, case_string):
        result = True
       
    result = 'YES' if result else 'NO'
    return result

#input, solve and output:
                        
input = open('C-small-attempt4.in', 'r')
output = open('C-small-attempt4.out', 'w')
d = init()

num_cases = int(input.readline())
for case in range(1, num_cases+1):
        l, x = [int(n) for n in input.readline().split()]
        case_string = input.readline().strip()
        result = solve(l, x, case_string)

        result_string = 'Case #%s: %s\n' %(case, result)
        print result_string
        output.write(result_string)

input.close()
output.close()
