# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
'''
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options
'''
import time
#t0=time.clock()

def split(item):
    size=item[0]
    freq=item[1]
    half=size/2
    if (size%2)==1:
        return [[half,2*freq]]
    else:
        return [[half,freq],[half-1,freq]]
    
t = int(raw_input())  # read a line with a single integer
for tr in xrange(1, t + 1):
    N, k = [int(s) for s in raw_input().split(" ")]

    gaps=[[N,1]]
    currently=0
    left=k
    while left>gaps[currently][1]:
        result=split(gaps[currently])
        if result[0][0]==gaps[-1][0]:
            gaps[-1][1]+=result[0][1]
            result=result[1:]
        gaps.extend(result)
        left-=gaps[currently][1]
        currently+=1
    size=gaps[currently][0]
    half=size/2
    bigger=half
    smaller=half
    if (size%2)==0:
        smaller-=1        
            
    print "Case #{}: {} {}".format(tr, bigger,smaller)
            
    
#print time.clock()-t0