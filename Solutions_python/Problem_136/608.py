import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        line = sys.stdin.readline().strip()
        arr = line.split(" ")
        C = float(arr[0].strip())
        F = float(arr[1].strip())
        X = float(arr[2].strip())
        current = 0
        currentRate = 2.0
        result = 0
        while True:
            if C / currentRate + X / (currentRate + F) >= X / currentRate:
                result += X / currentRate
                break
            result += C / currentRate
            currentRate += F

        print "Case #%d: %.07f" % (i + 1, result)
