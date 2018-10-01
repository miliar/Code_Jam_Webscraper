def iter(A):

    for n in range(len(A)-1):

        if A[n+1] < A[n]:

            A[n] -= 1

            break

    for k in range(n+1,len(A)):

        A[k] = 9

def tidy(A):

    for n in range(len(A)-1):

        if A[n+1] < A[n]:

            return(0)

    return 1


for tests in range(int(input())):

    n = [int(i) for i in input()]

    while not tidy(n):

        iter(n)

    
    s = ''.join(str(i) for i in n)

    leading_zero_index = 0

    while s[leading_zero_index]=='0':

        leading_zero_index+=1

    output = 'Case #'+str(1+tests)+': '+str(s[leading_zero_index:])

    print(output)
    
