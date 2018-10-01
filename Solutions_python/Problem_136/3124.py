
import sys
from time import sleep

def readIn():
    return [ float(n) for n in sys.stdin.readline().strip().split(' ') ]

def testCase():

    def recalcCookies( time, deltaTime, rate, cookies ):
        time += deltaTime
        cookies += rate * deltaTime
        return ( time, cookies )

    c,f,x = readIn()
    time = 0
    cookies = 0
    rate = 2

    while cookies < x:
        timeTillFarm  = ( c - cookies ) / ( rate )
        timeTillTotal = ( x - cookies ) / rate

        if cookies - c > 0:
            timeWithFarm = ( x - (cookies - c) ) / ( rate + f )
        else:
            timeWithFarm = x / ( rate + f ) + timeTillFarm

        if timeWithFarm < timeTillTotal:
            time, cookies = recalcCookies( time, timeTillFarm, rate, cookies )
            cookies -= c
            rate += f

        else:
            time, cookies = recalcCookies( time, timeTillTotal, rate, cookies )

    return time

def main():
    numCases, = readIn()
    num = 1

    while num <= numCases:
        time = testCase()
        print "Case #%d: %.7f" % (num, time)
        num += 1

main()
