# coding: utf-8

def result(n, k):
    for i in range(n):
        if (k >> i) & 1 == 0:
            return "OFF"
    return "ON"

def main():
    tcase = input()
    for t in range(tcase):
        n,k = map(int, raw_input().split(" "))
        print "Case #%d: %s" % (t + 1, result(n,k))

if __name__ == '__main__':
    main()
