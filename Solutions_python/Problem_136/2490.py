f = open('D:/B-large.in', 'r')
out = open('D:/out.txt', 'w')
T = int(f.readline().strip())
for j in range(T):
    C, F, X = map(float, f.readline().strip().split(" "))
    startPerSecond = 2
    timeToBuyFarms = 0
    while True:
        time = X/startPerSecond
        toNextFarm = C/startPerSecond + X/(startPerSecond + F)
        #print("time "+str(time)+"; to next farm "+str(toNextFarm)+"; start per second "+str(startPerSecond)+"; time to buy farms "+str(timeToBuyFarms))
        if time < toNextFarm:
            #print("Case #"+str(j+1)+": %.7f" % (timeToBuyFarms+time))
            out.write('Case #'+str(j+1)+': %.7f' % (timeToBuyFarms+time))
            out.write('\n')
            break
        else:
            timeToBuyFarms += (C/startPerSecond)
            startPerSecond+=F