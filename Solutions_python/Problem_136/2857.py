import sys


def input_generator():
    for line in sys.stdin:
        for token in line[:-1].split(' '):
            if token != '' or token:
                yield token

myin = input_generator()

def calcBestTime(C, F, X):
    rate = 2.0
    minTime = X / rate
    tElapsed = 0

    while True:
        tElapsed += C / rate
        rate += F
        curTime = tElapsed + (X / rate)
        if curTime > minTime:
            return minTime
        else:
            minTime = curTime

if __name__ == '__main__':
    tests = int(myin.next())
    for t in range(tests):
        minTime = calcBestTime(float(myin.next()), float(myin.next()), float(myin.next()))
        print 'Case #' + str(t+1) + ': ' + str(minTime)
