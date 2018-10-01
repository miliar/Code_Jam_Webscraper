from math import *

class Time:
    def __init__ (self, str):
        hr, mn = str.split(":")
        self.hour = int(hr)
        self.min = int(mn)
    
    def compare (self, next):
        if self.hour > next.hour:
            return "greater"
        elif self.hour < next.hour:
            return "smaller"
        elif self.min > next.min:
            return "greater"
        elif self.min < next.min:
            return "smaller"
        else:
            return "equal"

    def addTime (self, m):
        self.min += m
        while self.min >= 60:
            self.min -= 60
            self.hour += 1

def timeSort (X):
    for i in range (len (X) - 1):
        for j in range (len (X) - i - 1):
            if X[j+1][0].compare(X[j][0]) == "smaller":
                X[j+1], X[j] = X[j], X[j+1]
            elif X[j+1][0].compare(X[j][0]) == "equal" and X[j+1][1] == "arr" and X[j][1] == "dep":
                X[j+1], X[j] = X[j], X[j+1]


f = open("abc.in")
w = open("output.ot", 'w')
N = int (f.readline().strip())

for i in range(N):
    tabA = []
    tabB = []
    ttt = int (f.readline().strip())
    NA, NB = f.readline().strip().split(" ")
    NA = int (NA)
    NB = int (NB)
    for x in range(NA):
        dep, arr = f.readline().strip().split(" ")
        Barr = Time(arr)
        Barr.addTime (ttt)
        tabA.append ([Time(dep), "dep"])
        tabB.append ([Barr, "arr"])
    for y in range(NB):
        dep1, arr1 = f.readline().strip().split(" ")
        Aarr = Time(arr1)
        Aarr.addTime (ttt)
        tabB.append ([Time(dep1), "dep"])
        tabA.append ([Aarr, "arr"])
    timeSort (tabA)
    timeSort (tabB)
    A, B = 0, 0
    trainA, trainB = 0, 0
    for train in tabA:
        if train[1] == "dep":
            trainA -= 1
        else:
            trainA += 1
        if trainA < A:
            A = trainA
    for train in tabB:
        if train[1] == "dep":
            trainB -= 1
        else:
            trainB += 1
        if trainB < B:
            B = trainB
    
    result = "Case #%d: %d %d" % ((i +1), abs(A), abs(B)) + "\n"
    w.write(result)
f.close()
w.close()



