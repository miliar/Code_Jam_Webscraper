import sys

sys.stdin = open("A.in","r")
sys.stdout = open("A.out","w")
T = int(raw_input())
for i in xrange(T):
      n = int(raw_input())
      a = map(int,raw_input().strip().split())
      b = map(int,raw_input().strip().split())

      a.sort()
      b.sort()
      b.reverse()
      temp = sum(map(lambda x,y:x*y,a,b))
      print "Case #%s: %s" % (str(i+1),str(temp))

sys.stdin.close()
sys.stdout.close()
            
