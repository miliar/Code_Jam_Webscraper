#Tested locally with Python 2.6.2 on OS X 10.6.3
import math

input = open('C-small.in','r')
output = open('C-small.out','w')
T = int(input.next())

for i in range(0,T):
    numsonein = input.next().split(' ')
    groups = input.next().split(' ')
    R = int(numsonein[0])
    k = int(numsonein[1])
    N = int(numsonein[2])

    numPeople = 0
    totalMoney = 0
    for j in range(0,R):
        for l in range(0,N):
            if numPeople+int(groups[0]) <= k:
                numPeople+=int(groups[0])
                groups.append(groups.pop(0))
            else:
                totalMoney+=numPeople
                numPeople=0
                break
            if l == (N-1):
                totalMoney += numPeople
                numPeople=0

    output.write("Case #"+str(i+1)+": "+str(totalMoney)+"\n")
