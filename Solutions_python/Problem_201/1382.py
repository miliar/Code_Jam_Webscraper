# (c) 2017 Tuan Tran
import sys
import math

def log2(n):
    return n.bit_length() - 1

def max_remain(n, k):
    return math.ceil((n - k + 1) / (2 ** (log2(k))))

def min_max_distance(n, k):
    return ((max_remain(n, k) - 1) //2, max_remain(n, k) //2)

if __name__ == "__main__":
    time = int(sys.stdin.readline())
    target = open('c-output.txt', 'w')
    for i in range(time):
        line = sys.stdin.readline().split(' ')
        (min_dist, max_dist) = min_max_distance(int(line[0]), int(line[1]))
        target.write("case #{}: {} {}\n".format(i+1, max_dist, min_dist))
