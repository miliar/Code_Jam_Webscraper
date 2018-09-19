import sys

result = ""
def list(N, P):
    result = ""
    if N is 0: 
        return
    if P>2**(N-1):
        result += 'L'
        list(N-1,P-(2**(N-1)))
    else:
        result += 'W'
        list(N-1,P)

def getbest(N, p):
    ans = 2**N - p
    c = 0
    while ans is not 0: 
        c += 1
        ans = ans*2
    re = ""
    for i in range(i, c):
        re += 'W'
    for i in range(c, N):
        re += 'L'
    return re;

def getworst(N, p):
    ans = p+1
    c = 0
    while ans is not 0:
        c = c+1
        ans = ans*2
        re =""
        for i in range(i, c):
            re += 'W'
        for i in range(c, N):
            re += 'L'
    return re;

def findworst(standard, N):
    left = 0
    right = 2**N - 1
    while left < right:
        mid = (left + right) / 2 
        if(getworst(N,mid) < standard):
            left = mid+1;
        else:
            right = mid;
    return left

def findbest(standard, N):
    left = 0
    right = 2**N - 1
    while left < right:
        mid = (left + right) / 2 
        if(getworst(N,mid) < standard):
            left = mid;
        else:
            right = mid+1;
    return left


T = int(raw_input())
for i in range(1, T):
    in_string = raw_input()
    in_vector = in_string.split(" ")
    N = int(in_vector[0])
    P = int(in_vector[1])
    result = ""
    list(N,P)
    standard = result
    record1 = findworst(standard,N)
    result = ""
    list(N,P+1)
    standard = result
    record2 = findbest(standard,N);
    sys.stdout.write("Case #"+str(c)+": "+str(record1)+" "+str(record2-1)+"\n")
