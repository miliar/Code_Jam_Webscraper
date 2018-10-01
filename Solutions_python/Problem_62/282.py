#-*- coding:utf-8 -*-
#!/usr/bin/env/python
def readInt(): return int(raw_input())
def readArray(num_):
    result = []
    for i in xrange(num_):
        result.append(map(int,raw_input().split()))
    return result
def countIntersectionPoint(points_):
    result = 0
    size = len(points_)
    for i in xrange(size):
        for j in xrange(i+1,size):
            a1 = float(points_[i][1]-points_[i][0])
            a2 = float(points_[j][1]-points_[j][0])
            b1 = float(points_[i][0])
            b2 = float(points_[j][0])
            if a1==a2:
                if b1==b2:
                    result += 1
            elif 0<=(b2-b1)/(a1-a2)<=1:
                result += 1
    return result

def main():
    T = readInt()
    for i in xrange(T):
        N = readInt()
        points = readArray(N)
        print "Case #%d: %d" %(i+1,countIntersectionPoint(points))
if __name__ == '__main__':
    main()
