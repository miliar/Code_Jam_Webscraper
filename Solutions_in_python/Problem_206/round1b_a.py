#! coding: utf-8
 
if __name__ == '__main__':

    
    #python2:
    T = int(raw_input())
    for i in xrange(T):
        D, N = [int(s) for s in raw_input().split(" ")]
        data = []
        for j in xrange(N):
            k, s = [int(s) for s in raw_input().split(" ")]
            data.append([k,s])
        data.sort(key = lambda x: x[0])
        minv = []
        while len(data) > 1:
            if data[1][1] == data[0][1]:
                del data[1]
            elif data[0][1] < data[1][1]:
                del data[1]
            elif (float(data[1][0] - data[0][0]) / float(data[0][1] - data[1][1]) <
                  float(D - data[1][0]) / float(data[1][1]) ):
                del data[0]
            else:
                del data[1]

        res = float(D) * float(data[0][1]) / float(D - data[0][0]) 
        print("Case #{0}: {1}".format(i + 1, res))
         
        

