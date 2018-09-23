import sys
sys.stdout = open('PanckageFliper.txt', 'w')

def inputIntegerArray():
    return list( map( int, input().split(" ") ) )

def flip( pattern, i ):
    if pattern[i]=='+':
        pattern[i] = '-'
    else:
        pattern[i] = '+'

def solve( pattern, k ):
    flips = 0;
    for i in range(0, len(pattern) - k + 1):
        if pattern[i] == '-':
            for j in range(i,i+k):
                flip(pattern,j)
            flips += 1

    for i in range(0,len(pattern)):
        if pattern[i] == '-':
            return -1
    return flips

n = inputIntegerArray()[0]
for test in range(1,n+1):
    (pattern,k) = input().split(" ")
    answer = solve( list(pattern), int(k) )

    #print ( solve( list(pattern), int(k) ),  solve( list(pattern)[::-1], int(k) ) );

    if  answer >= 0 :
        print ( "Case #{}: {}".format( test, answer ) )
    else:
        print("Case #{}: {}".format(test, "IMPOSSIBLE" ) )

