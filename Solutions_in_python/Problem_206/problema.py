def solv(D, pairs):
    h = 0
    for d, v in pairs:
        h = max(h, (D - d) / float(v))
    return D/h

def main():
    n = int(raw_input())
    for i in range(n):
        D, m = map(int, raw_input().split(' '))
        a = []
        for j in range(m):
            a.append(map(int, raw_input().split(' ')))
        res = solv(D, a)
        print "Case #%d: %6f" %(i+1, res)

if __name__ == "__main__":
    main()