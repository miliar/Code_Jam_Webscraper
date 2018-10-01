
M = {'1': 1, 'i': 2, 'j': 3, 'k': 4}

multiply_table = [
        None, 
        [None, 1, 2, 3, 4], 
        [None, 2, -1, 4, -3], 
        [None, 3, -4, -1, 2], 
        [None, 4, 3, -2, -1]] 

divide_table = [
        None, 
        [None, 1, -2, -3, -4], 
        [None, 2, 1, 4, -3], 
        [None, 3, -4, 1, 2], 
        [None, 4, 3, -2, 1]] 

def mul(a, b): 
    if a * b > 0: 
        return multiply_table[abs(a)][abs(b)]
    return -multiply_table[abs(a)][abs(b)]

def div(c, a): 
    if c * a > 0: 
        return divide_table[abs(c)][abs(a)]
    return -divide_table[abs(c)][abs(a)]

def check(N, H): 
    n = len(H) 

    if n < 3: 
        return False 

    if 3 not in N and 4 not in N: 
        return False

    for i in range(n-2): 
        a = H[i] 
        if a == 2: 
            for j in range(i+1, n-1): 
                b = div(H[j], H[i]) 
                c = div(H[-1], H[j]) 

                if b == 3 and c == 4: 
                    return True 

    return False

T = input() 

for t in range(T): 
    _, x = map(int, raw_input().split()) 
    L = raw_input() 
    S = L * x 

    N = map(lambda s: M[s], S) 
    # print N 
    n = len(N)

    H = list(N) 

    for i in range(1, n): 
        H[i] = mul(H[i-1], H[i]) 

    # print H 

    print 'Case #%d:' %(t+1),
    if check(N, H): 
        print 'YES' 
    else: 
        print 'NO' 
    
