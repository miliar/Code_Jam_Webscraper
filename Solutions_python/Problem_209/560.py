import sys
import math
import heapq

name = "A-large"
path = "/Users/hao/Desktop/"

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(raw_input())


def cal(rec, k):
    area = 0
    for i in range(k - 1, len(rec)):
        tmp = math.pi * rec[i][0] * rec[i][0]
        tmp += 2 * math.pi * rec[i][1] * rec[i][0]
        lst = []
        for j in range(i):
            lst.append(rec[j][1] * rec[j][0] * 2 * math.pi)
        lst.sort()
        if k > 1:
            tmp += sum(lst[-k+1:])
        area = max(area, tmp)
    return area


for testCase in range(1, testCases + 1):
    line = raw_input().split()
    N = int(line[0])
    K = int(line[1])
    rec = []
    for pk in range(N):
        line = raw_input().split()
        rec.append((int(line[0]), int(line[1])))
    rec.sort()
    area = cal(rec, K)
    print 'Case #%s: %.9f' % (testCase, area)
    