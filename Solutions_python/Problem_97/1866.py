import sys

def solve(n, m):
    countMap = {}
    for i in range(n,m):
        original = str(i)
        allRotation = [original[x:]+original[:x] for x in range(1, len(original))]
        for rot in set(allRotation):
            if int(original)<int(rot)<=m:
                if rot not in countMap:
                    countMap[rot] = 1
                else:
                    countMap[rot] += 1
    return sum(countMap.values()) 
 
if __name__ == '__main__':
    fileName = sys.argv[1]
    with open(fileName + '.in') as data:
        T = int(data.readline().strip())
        for i in range(T):
            s = data.readline().strip()
            n,m = [int(x) for x in s.split()]
            print "Case #%s: %s" % (i+1, solve(n,m))
