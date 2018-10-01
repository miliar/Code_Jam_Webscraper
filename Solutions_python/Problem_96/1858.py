from os import sys
from bisect import bisect_right, bisect_left
def solve(no_sup,p,scores):
    if(p==0):return len(scores)
    scores.sort()
    hi = max(3*p-3,3)
    low = max(3*p-4,2)
    m = bisect_right(scores,hi) - bisect_left(scores,low)
    hi = len(scores)-bisect_right(scores,hi)
    print p,scores
    print m, hi
    if m>=no_sup:
       return no_sup+hi
    return m+hi


if __name__=="__main__":
   source = file(sys.argv[1])
   sink = file(sys.argv[1].replace(".in","")+".out",'w')
   for c,i in enumerate(source):
          if(c>0):
              k = [int(t) for t in i.split()]
              sink.write("Case #"+str(c)+": "+ str(solve(k[1],k[2],k[3:]))+"\n")
   sink.close()
   source.close()
