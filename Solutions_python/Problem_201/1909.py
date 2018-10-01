from collections import deque
import time
import math

def main():
    path = "C:\\Users\\user\\Dropbox\\Documents\\GoogleCodeJam2017\\C.Toilets\\"
    with open(path + "result" + str(time.time()) + ".txt", 'w') as resF:
        T, N, K = readFile(path + "c2_2.in")#####
        for i in xrange(T):
            t = time.time()
            (maxi, mini) = solve2(N[i], K[i])
            #print str(i) + ": " + str(maxi) + " " + str(mini)
            resF.write("Case #" + str(i+1) + ": " + str(maxi) + " " + str(mini) + "\n")


def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        if len(lines) == 0:
            print "Err reading"
        T = int(lines[0].replace("\n", ""))

        N = []
        K = []
        for i in xrange(1, T+1):
            temp = lines[i].split(" ")
            N.append(int(temp[0]))
            K.append(int(temp[1].replace("\n", "")))

        return (T, N, K)


def solve(n, k):

    lastone = n+1
    bars = [lastone]
    for i in xrange(k):
        chosen = max(bars)
        lastone = chosen
        bars.remove(chosen)
        bars.append(math.ceil(float(chosen)/2))
        bars.append(math.floor(float(chosen)/2))
    return (int(math.floor(float(lastone)/2)-1), int(math.ceil(float(lastone)/2)-1))


def solve2(N, K):
    N += 1
    n = long(math.floor(math.log(K, 2)))
    m = long(1 << n)
    t = N / m
    b = N - t * m
    finale = float(t)
    #print b-K+m
    if b > K - m:
        finale += 1
    if finale % 2 == 0:
    #    print "Wopeee"
        return long(finale/2) - 1, long(finale/2) -1
    return long(finale/2), long(finale/2) -1




if __name__ == '__main__':
    #x,y = solve2(999999,127)
    #x,y = solve2(500000000000000000, 127)
    #x,y = solve2(500000, 128)

    #print "%d %d" % (x,y)
    main()


