import sys
sys.stdout = open('CruiseControl.out', 'w')

def inputArray( type ):
    return list( map( type, input().split(" ") ) )

n = int( input())

# def possible( D)
# def solve( D, N, data ):
#     left = 0.0
#     right = float(D)
#     for i in range(64):
#         m = ( left + right )/2;


for test in range(1,n+1):
    (D,N) = inputArray( int )
    data = []
    answer = None
    for i in range(N):
        (K,S) = inputArray( int )
        timeToDestination = (D-K)/S
        posibleSpeed = D/timeToDestination
        if answer is None:
            answer = posibleSpeed
        else:
            answer = min(answer, posibleSpeed )

    print("Case #{}: {}".format(test, answer ))