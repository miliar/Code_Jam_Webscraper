import sys

def getSpeed(C, F, X):
    speed = 2.0
    t = 0.0
    while True:
        t1 = X / speed # keep
        t2 = C / speed + X / (speed + F) # farm
        if t1 <= t2:
            return t + t1
        else:
            t += C / speed
            speed += F

def main():
    T = int(sys.stdin.readline())
    for prob in range(T):
        C, F, X = [float(i) for i in sys.stdin.readline().split()]
        t = getSpeed(C, F, X)
        print "Case #{0}: {1}".format(prob + 1, t)

main()
