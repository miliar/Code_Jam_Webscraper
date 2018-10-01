__author__ = 'GerasimFromUkraine'



import math

fp = open('input/C-small-attempt2.in', 'r')
out = open('output/output.out', 'w')

cc = 0
for i in fp:

  cnt = 0
  a,b =  map(int, i.split())
  # print math.sqrt(a)
  # print math.sqrt(b)
  a = int(math.ceil(math.sqrt(a)))
  b = int(math.floor(math.sqrt(b)))
  for n in xrange(a, b+1):
    oN = n
    n *= n
    # print n
    sN = str(n)
    sL = len(sN)/2
    cnt += 1
    #todo function with recursion
    for c in xrange(0, sL):
      if sN[c] != sN[-1-c]:
        cnt -= 1 #cnt +- 1 ???
        break
      elif c == sL-1:
        # print n, oN
        soN = str(oN)
        onL = len(soN)/2
        for ch in xrange(0, onL):
          if soN[c] != soN[-1-ch]:
            cnt -= 1 #cnt +- 1 ???
            break
  # print a,b
  cc +=1
  output = 'Case #'+ str(cc) +': ' + str(cnt) + '\n'
  print output
  out.write(output)
  # print a,'-', b
fp.close()
out.close()