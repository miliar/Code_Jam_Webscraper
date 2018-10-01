from collections import Counter

def is_palindrome(n):

    s = str(n)
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]: return False
    return True

fair_and_square_number = []

def preprocess():
    for i in range(1, 10000001):
        if is_palindrome(i) and is_palindrome(i*i): fair_and_square_number.append(i*i)
    print fair_and_square_number


def solve(A, B):

    count = 0
    for n in fair_and_square_number:
        if A <= n <= B: count += 1
    print count
    return count


if __name__ == '__main__':

    import sys
    
    input_file = sys.argv[1]
    output_file = input_file[:].replace('.in', '.out')


    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')

    T, = [int(x) for x in f_in.readline().split()]
    preprocess()

    for case in range(1, T+1):
        print 
        print '====================='
        print '    ' + str(case)
        print '====================='

        A, B = [int(x) for x in f_in.readline().split()]

        # Solve
        ans = solve(A, B)

        ## Output
        f_out.write('Case #%d: %s\n' % (case, ans))

        

