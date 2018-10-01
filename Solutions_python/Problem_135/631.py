import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        first = int(sys.stdin.readline().strip())
        firstSet = set()
        for j in range(4):
            line = sys.stdin.readline().strip()
            if j + 1 == first:
                arr = line.split(" ")
                for num in arr:
                    firstSet.add(int(num.strip()))

        second = int(sys.stdin.readline().strip())
        secondSet = set()
        for j in range(4):
            line = sys.stdin.readline().strip()
            if j + 1 == second:
                arr = line.split(" ")
                for num in arr:
                    secondSet.add(int(num.strip()))

        intersection = firstSet.intersection(secondSet)
        n = len(intersection)
        if n == 0:
            print "Case #%d: Volunteer cheated!" % (i + 1)
        elif n > 1:
            print "Case #%d: Bad magician!" % (i + 1)
        else:
            print "Case #%d: %d" % (i + 1, list(intersection)[0])
