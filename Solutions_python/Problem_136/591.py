import sys 
import string
from collections import *

def intersect(a, b):
	return list(set(a) & set(b))

f = open(sys.argv[1])

T = int(f.readline())
for c in xrange(1, T+1): 
 line = f.readline().split(' ')
 C = float(line[0])
 F = float(line[1])
 X = float(line[2])
 rate = 2.0 
 time = 0.0
 timetoC = X/rate
 timetofarm = C/rate + (X/ (rate + F))
 #print timetoC
 #print timetofarm
 while(timetofarm<timetoC):
    time += C/rate
    rate += F
    timetoC = X/rate
    timetofarm = C/rate + (X/ (rate + F))
    #print 'rate ' + str(rate)
    #print 'ttf ' + str(timetofarm)
    #print 'ttc ' + str(timetoC)
    #print 'time ' + str(time)
 time += timetoC
 print 'Case #' + str(c) + ': ' + str(time)
	
#you get cookies continuously so 0.1s after start you have 0.2 cookies. you have production * time cookies. 

#while the amount of time taken to buy a farm and then get to C cookies is faster than the time taken to just get to C cookies, buy anohter farm 




