
"""
Determines whether an input number is a tidy number.

Arguments:
    x - an integer
Returns:
    a boolean value corresponding to whether the input is a tidy number.
"""
def isTidy(x):

    s = str(x)

    for i in range( len(s) - 1 ):
        if int( s[i] ) > int( s[i+1] ):
            return False

    return True

"""
Finds the largest tidy number less (or equal to) some input number.

Arguments:
    x - an integer
Returns:
    an integer which is a tidy number
"""
def previousTidy(x):
    if isTidy(x):
        return x

    #find the first 'fall'
    s = list( str(x) )

    for i in range( len(s) - 1 ):
        if int( s[i] ) > int( s[i+1] ):
            pointer = i+1
            break

    #go back through until a rise
    for i in range(pointer, 0, -1):
        if int( s[i] ) > int( s[i-1] ):
            pointer = i+1
            break
        elif i == 1:
            pointer = 1
            break

    for i in range( pointer, len(s) ):
        s[i] = '0'

    prev = int( "".join(s) ) - 1

    assert isTidy(prev)

    return prev

def main():
    testCases = int( input() )

    for test in range(1, testCases + 1):
        prevTidy = previousTidy( int( input() ) )
        print( "Case #" + str(test) + ": " + str(prevTidy) )

if __name__ == '__main__':
    main()
