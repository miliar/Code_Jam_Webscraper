def timeNFarm(n, C, F):
    return C*1.0/(2 + n*F);
def timeToCollectCookies(n, X):
    return X*1.0/(2 + n*F);

fout = open('CookieAns.txt', 'w')
fin = open('B-large.in','r')
T = int(fin.readline())
for i in range(T):
    print i, T
    C, F, X = map(float, fin.readline().split());
    currentTime = 0;
    timeNextFarm = currentTime + timeNFarm(0, C, F);
    time = currentTime + timeToCollectCookies(0, X);
    nextTime = timeNextFarm + timeToCollectCookies(1, X);
    index = 1;
    while (nextTime < time):
        currentTime = timeNextFarm;
        timeNextFarm = currentTime + timeNFarm(index, C, F);
        time = currentTime + timeToCollectCookies(index, X);
        nextTime = timeNextFarm +timeToCollectCookies(index + 1, X);
        index += 1;
    fout.write('Case #' + str(i + 1) + ': ' +  "%.7f" % time + '\n');



fin.close()
fout.close()
        
