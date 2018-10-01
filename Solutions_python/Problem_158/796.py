import math
#INPUT_FILE = 'A-large.in'
#OUTPUT_FILE = 'A-large.out'

INPUT_FILE = 'D-small-attempt3.in'
OUTPUT_FILE = 'D-small-attempt3.out'

#INPUT_FILE = 'sample.in'
#OUTPUT_FILE = 'sample.out'


def solve(X, R, C):
    result = 'GABRIEL'
    '''
    if X == 2:
        if R%2 or C%2:
            result = 'RICHARD'
    '''
    
    if (math.ceil(X/2.) > R or 
        math.ceil(X/2.) > C or
        (X > R and X > C) or 
        (R * C) % X):
        result = 'RICHARD'
    if X == 4:
        if (R <= 2 or C <= 2):
            result = 'RICHARD'

    return result


def main():
    f_in = open(INPUT_FILE, 'r')
    f_out = open(OUTPUT_FILE, 'w')
    T = int(f_in.readline())
    for t in xrange(T):
        tokens = f_in.readline().split()
        result = solve(int(tokens[0]), int(tokens[1]), int(tokens[2]))
        f_out.write('Case #%d: %s\n' % (t+1, result))
    f_out.close()
    f_in.close()

if __name__ == '__main__':
    main()