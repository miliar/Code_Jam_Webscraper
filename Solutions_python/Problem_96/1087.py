from numpy import*

## code jam 2012, question B.

filename = "B-large.in.txt"
FILE = open(filename, "r")
N = int(FILE.readline())

for k in range(N):
    T = map(int, FILE.readline().split())

    n = T[0]
    s = T[1]
    p = T[2]
    T = T[3:]
    #print n,s,p,T
    # T is now list of total scores...
    num1 = 0
    num2 = 0
    ans = 0
    for i in range(len(T)):
        if ( T[i] >= 3*p - 2)&(T[i] >= p):#(T[i]/3. > 0):
            num1 += 1
        elif ( T[i] >= 3*p-4 )&(T[i] >= p):#(T[i]/3. > 0):
            num2 += 1
    #print num1, num2
    ans += num1
    if (s >= num2):
        ans += num2
    else:
        ans += s
    print "Case #%d: %d"%(k+1, ans)
    
