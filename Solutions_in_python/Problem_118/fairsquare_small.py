import sys
import math

rl = sys.stdin.readline

def GenerateFairSqr(start, end):
    begin_base = math.ceil(math.sqrt(start))
    end_base = math.floor(math.sqrt(end)) + 1
    # print("%d ,%d"%(begin_base, end_base))
    for i in range(begin_base, end_base):
        #print(i)
        if str(i) != str(i)[::-1]:
            continue
        sqrd = i**2
        str_isqr = str(sqrd)
        if str_isqr == str_isqr[::-1]:
            # print(sqrd)
            yield sqrd

def Main():
    n = int(rl())
    for i in range(n):
        a, b = map(int, rl().strip().split(" "))
        print("Case #%d: %d"%( i+1, len(list(GenerateFairSqr(a,b)))))

Main()