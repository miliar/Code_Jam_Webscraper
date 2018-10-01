import numpy as np

def convertToArray(N):
    num = []
    while N > 0:
        num =  [N%10]+num 
        N = N - N%10
        N = int(N/10)
    return num


def mnm(X):
    maxi,mini = 0,0 
    for i in range(len(X)):
        if i == len(X) -1:
            maxi =  i
            break
        elif X[i] > X[i+1]:
            maxi =  i
            break
    for i in range(len(X)):
        if X[i] == X[maxi]:
            mini = i
            break
    return mini,maxi


def main(n):
    x = convertToArray(n)
    mini,maxi = mnm(x)
    if maxi == len(x) - 1:
        return n
    digit = 0
    summ = 0
    for i in  range(mini):
        summ = 10*summ + x[i]
    i = mini
    summ = 10 * summ + x[mini]-1
    while i < len(x)-1:
        summ = 10*summ + 9
        i = i +1
    return summ


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(main(int(input())))
    print("Case #{}: {}".format(i, n))
