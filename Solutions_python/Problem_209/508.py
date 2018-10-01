import math
if __name__ == '__main__':
    PIE = math.pi
    fo = open("1.out", "w")
    fi = open("A-large.in", "r")
    T = int(fi.readline())
    for tt in range(T):
        (N, K) = [int(x) for x in fi.readline().split(' ')]
        bing = [[float(int(x)) for x in fi.readline().split(' ')] for i in range(N)]
        for i in bing:
            i.insert(0, 2*i[1]*i[0])
        bing.sort()
        sum_num = 0
        max_r = -1
        max_p = -1

        for i in range(N-K, N):
            if(bing[i][1] > max_r):
                max_r = bing[i][1]
                max_p = i
            sum_num += bing[i][0]
        print(bing)
        delta = bing[max_p][1] * bing[max_p][1]
        for i in range(0, N-K):
            if(bing[i][1] > bing[max_p][1]):
                print(bing[i][1]*bing[i][1]+bing[i][1]*2*bing[i][2])
                print(bing[max_p][0])
                print(delta)
                if(bing[i][1]*bing[i][1]+bing[i][1]*2*bing[i][2] - bing[N-K][0] > delta):
                    delta = bing[i][1]*bing[i][1]+bing[i][1]*2*bing[i][2] - bing[N-K][0]
        print(delta)
        fo.write('Case #{0}: {1:.8f}\n'.format(tt + 1, (sum_num+delta)*PIE))
