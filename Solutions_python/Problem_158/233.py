def solve(x, r, c):
    result = 'GABRIEL'
    print x, r, c


    # gap in the middle
    if x >= 7:
        return 'RICHARD'

    # gaps left
    elif (r * c) % x != 0:
        return 'RICHARD'

    # n-omino too large
    elif x > (r * c):
        return 'RICHARD'

    # n-omino width > grid width
    elif x - x/2 > min(r, c):
        return 'RICHARD'


      
    # only one possible 1-ominoes
    # only one possible 2-ominoes
    elif x == 1 or x == 2:
        return 'GABRIEL'

    # two possible 3-ominoes  
    elif x == 3:
        return 'GABRIEL'

    # five possible 4-ominoes
    elif x == 4:
        if min(r, c) <= 2:
            return 'RICHARD'
        else:
            return 'GABRIEL'

    # x possible 5-ominoes
    elif x == 5:
        if min(r, c) <= 2:
            return 'RICHARD'
        elif r * c <= 15:
            return 'RICHARD'
        else:
            return 'GABRIEL'

    # x possible 6-ominoes
    elif x == 6:
        if min(r, c) <= 3:
            return 'RICHARD'
        elif r * c <= 18:
            return 'RICHARD'
        else:
            return 'GABRIEL'
        

    return result

#input, solve and output:
                        
input = open('D-large.in', 'r')
output = open('D-large.out', 'w')


num_cases = int(input.readline())
for case in range(1, num_cases+1):
        x, r, c = [int(n) for n in input.readline().split()]
        result = solve(x, r, c)

        result_string = 'Case #%s: %s\n' %(case, result)
        print result_string
        output.write(result_string)

input.close()
output.close()
