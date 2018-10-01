import math
#------------------------------------------------------------------------
#min_max function
#------------------------------------------------------------------------
def find_group(ni, ai, bi):
    ss = int(ni/ai)

    if bi<=(ni-ss*ai):
        return ss+1
    else:
        return ss
#------------------------------------------------------------------------
#min_max function
#------------------------------------------------------------------------
def min_max(c):
    if c%2 == 1:
        m = (c-1)/2
        return m, m
    elif c == 0:
        return 0,0
    else:
        m1 = c/2
        m2 = (c-2)/2
        return m1, m2
    
#------------------------------------------------------------------------
#Solve function
#------------------------------------------------------------------------
def solve(i_int_list):
    n = i_int_list[0]
    k = i_int_list[1]

    a = math.pow(2, int(math.log(k, 2))) #number of different seat groups

    n = n-a+1 #remaining seats

    b = k - (a-1) #priority
    
    c = find_group(n, a, b)

    
    return min_max(c)
    
#------------------------------------------------------------------------
#Simple tests
#------------------------------------------------------------------------
if False:
    simple_test_input_1 = "1000"
    simple_test_input_2 = "1000"
    
    test_list = []
    int_list  = []
    int_list.append(int(simple_test_input_1))
    int_list.append(int(simple_test_input_2))
    test_list.append(int_list)

    print(solve(test_list[0]))
#------------------------------------------------------------------------
#Read Code Jam input file for integers and Write output
#------------------------------------------------------------------------
if True:
    t = int(raw_input())
    test_list = []
    for i in range(0, t):
        int_list = []
        for s in raw_input().split(" "): #split(",")
            int_list.append(int(s))
        test_list.append(int_list)
        #*****
        res = solve(test_list[i])
        #*****
        #Write to output file
        print(("Case #{}: {} {}").format(i+1, res[0], res[1]))
