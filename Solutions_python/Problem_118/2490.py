from sys import argv


def extract_input( filename ):
    try:
        print "Your first variable is:", filename
        file = open(filename, 'a+')
        out_file = open('out', 'a+')
        no_of_input = int(file.readline())

        index = 1

        for lines in file.readlines():
            line = lines.split('\n')[0]
            if line !='\n' and len(line):
                out_file.write( 'Case #%s: %s\n' %( index, generate_output( line ) ))
                index+=1
    except Exception as e:
        print e

def generate_output( case ):
    split_case = case.split(' ')
    lower_bound = int(split_case[0])
    upper_bound = int(split_case[1])


    count = 0
    for num in range( lower_bound, upper_bound+1):
        check1, check2 =  ( check_palindrome( num ), check_square( num ) )
        if check1 and check2:
            count+=1

    return count



def check_palindrome( num ):
    str_palin = str(num)
    if str_palin == str_palin[::-1]:
        return True
    return False

def check_square( num ):
    if (num <= 1):
        return True;

    currentSquare = 4;
    currentNumber = 2;

#    loop through till the num is more than
#    the square of the current number
    while currentSquare <= num :
#    if we have a match, return true
        if currentSquare == num:
            return check_palindrome( currentNumber)
        #increment current number
        currentNumber+=1;
        #find the next square
        currentSquare = currentNumber * currentNumber;

    #no matching number could be squared
    return False;

if __name__ == '__main__':
    script, filename = argv
    extract_input( filename )
