
import sys

def Lawnmower(lawn, x, y):
    def CheckLine(l, px, py):
        pv = l[py][px]
        mx = max(l[py])
        my = 0
        for i in range(y):
            if l[i][px] > my:
                my = l[i][px]

        if my > pv and mx > pv:
            return False
        return True

    for i in range(y):
        for j in range(x):
            if not CheckLine(lawn, j, i): 
                return "NO"
    return "YES"

def runIt():
    input = sys.stdin
    n_tests = int(input.readline(), 10)
    
    for i in range(n_tests):
        lawn = []
        (y, x) = map(int, input.readline().split(' '))
        for j in range(y):
            line = input.readline().split(' ')
            line = map(int, line)
            lawn.append(line)
        result = Lawnmower(lawn, x, y)
        print ("Case #{0}: {1}".format(i + 1, Lawnmower(lawn, x, y)))

runIt()
