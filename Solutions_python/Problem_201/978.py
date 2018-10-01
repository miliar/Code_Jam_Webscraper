from math import log
num = input()
for ind in range(num):
    numStalls, numPeople = map(int, raw_input().split(" "))
    usedStalls = [0, numStalls+1]
    minStall = [-1, 10**30, (0,0)]
    level = int(log(numPeople,2))+1
    high = numStalls/(2**level)
    res = [high, high]
    numStalls -= numPeople
    i=0
    while 2**(level-1)*res[0]+2**(level-1)*res[1]>numStalls:
        res[i%2]-=1
        i+=1
    print "Case #%d: %d %d"%(ind+1,res[1],res[0])
