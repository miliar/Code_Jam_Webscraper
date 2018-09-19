import sys
import math

def initialize():
    file_in = 'D:\code jam\input.in'
    file_out = 'D:\code jam\output.txt'
    
    try:
        data_in  = open(file_in, 'r')
    except:
        print("Can't open file \'" + data_in +"\'")
        sys.exit()
    
    try:
        data_out  = open(file_out, 'w')
    except:
        print("Can't write to file \'" + data_out +"\'")
        sys.exit()

    return(data_in, data_out)

def get_variables():

    line = data_in.readline().split(' ')

    N=int(line[0])
    M=int(line[1])
    

#    print('N:', N)
#    print('M:', M)
#    print('b:', b)
#    print('p:', p)
#    print('points_list:', points_list)
    return(N,M)

def calculate_result(N,M):

    A = math.sqrt( N )
    B = math.sqrt( M )
    
    A = math.ceil( A )
    B = math.floor( B )
    
    print('A:', A, 'B:', B)

    result=0   
    while(A<=B):
        if is_palindrome(A):
            print('P:', A)
            square=A**2
            if is_palindrome(square):
                result+=1
        A+=1
     
    return result

def is_palindrome(num):
    n = num;
    rev = 0;
    while (num > 0):
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num // 10;
    
    if n==rev:
        return 1
    else:
        return 0
      

       
(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    N,M = get_variables()
    if(i==99):
        j=i
#        help('str')
    result = calculate_result(N,M)
    print( 'Case #' + str(i) + ': ' + str(result) )
    data_out.write( 'Case #' + str(i) + ': ' + str(result) + '\n' )
    


