import sys

sys.stdin = open("B-large.in", "r")
sys.stdout = open("B-large.txt", "w")

t = int(raw_input())

for test in xrange(t):
    c,f,x = map(float, raw_input().split())
    rate = 2
    totalTime = 0
    
    while True:
        secsToBuyFarm = c / rate
        if secsToBuyFarm + x / (rate+f) > x / rate:
            totalTime += x / rate
            break
        rate += f
        totalTime += secsToBuyFarm
        
    
    print("Case #" + str(test+1) + ": " + str(totalTime)) 