import sys

S = "welcome to code jam"

def count(str):
    pre = [Data(-1,1)]
    for c in S:
        cur = []
        for i in range(len(str)):
            if c == str[i]:
                sum = 0
                for tmp in pre:
                    if tmp.i < i:
                        sum += tmp.cnt
                cur.append(Data(i, sum))
        pre = cur
        if len(pre) == 0:
            break
    ret = 0
    for tmp in pre:
        ret += tmp.cnt
    return "%04d" % (ret % 10000)

class Data:
    def __init__(self, i, cnt):
        self.i = i
        self.cnt = cnt

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        print("Case #%d: %s" % (i+1, count(sys.stdin.readline())))

if __name__ == "__main__":
    main()