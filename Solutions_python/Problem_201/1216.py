from math import *

def f(n,k):
    if k == 0:
        #print("n = {} k = {}: {}".format(n,k,n))
        return n
    if k == 1:
        #print("n = {} k = {}: {}".format(n,k,ceil((n-1)/2)))
        return ceil((n-1)/2)

    if k == 2:
        #print("n = {} k = {}: {}".format(n,k,floor((n-1)/2)))
        return floor((n-1)/2)
    
    if n == 0:
        #print("n = {} k = {}: {}".format(n,k,0))
        return 0
    answer = max(f(floor((n-1)/2),floor((k-1)/2)),f(ceil((n-1)/2),ceil((k-1)/2)))
    #print("n = {} k = {}: {}".format(n,k,answer))
    return answer

##n = 1000
##for k in range(0,3):
##    print("n = {} k = {}: {}".format(n,k,f(n,k)))
##    #print()

def h(n,k):
    i = f(n,k)
    return (ceil((i-1)/2),floor((i-1)/2))

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    tup = h(n,k-1)
    print("Case #{}: {} {}".format(i, tup[0], tup[1]))
  # check out .format's specification for more formatting options
