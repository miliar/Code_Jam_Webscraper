import string

def tidy(name):
  file = open(name,'r')
  n = int(file.readline())
  for i in range(n):
    n = int(file.readline())
    find = False
    while (not find):
      thisn = n
      while thisn>0:
        last = thisn%10
        sndlast = (thisn/10)%10
        if last<sndlast:
          thisn = -1
          n -= 1
        elif thisn<10:
          thisn = -1
          find = True
        else:
          thisn = thisn/10
    print "Case #%d: %d" %(i+1,n)

tidy('B-small-attempt0.in')