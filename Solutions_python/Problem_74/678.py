#!/usr/bin/python -tt

import sys

def main():
    if len(sys.argv) != 2:
        print 'Requires input file'
        sys.exit()
    fname = sys.argv[1]
    fptr = open(fname, 'r')
    numtest = int(fptr.readline().split(' ')[0])
    outptr = open('output', 'w')
    for i in xrange(numtest):
        input = fptr.readline().split(' ')
        numinstr = int(input[0])
        #print numinstr
        #print input
        currpos = {'O': 1, 'B':1}
        currrobot = 'X'
        prevaction = 0
        tottime = 0
        for p in xrange(numinstr):
            j = 1 + p*2
            #print 'j is ', j
            robot = input[j]
            button = int(input[j+1])
            # calculate time for this move
            time = abs(button-currpos[robot])
            currpos[robot] = button
            #print 'Time %d newpos %d' % (time, currpos[robot])
            if robot != currrobot:
                currrobot = robot
                #print 'Robot changes to %s' % robot
                #print 'Prevaction = %d' % prevaction
                if time <= prevaction:
                    #print 'Time taken was lesser than prevaction'
                    # just add the time to press button
                    tottime = tottime + 1
                    prevaction = 1
                else:
                    #print 'Time taken was more than prevaction'
                    tottime = tottime + time - prevaction + 1
                    prevaction = time - prevaction + 1
                    #print 'New prevaction is %d' % prevaction
            else:
                tottime = tottime + time + 1
                prevaction = prevaction + time + 1
                #print 'More time = %d' % (time + 1)
                
        outptr.write('Case #%d: %d\n' % (i+1, tottime))
    
    outptr.close()
    fptr.close()
        

if __name__ == '__main__':
    main()