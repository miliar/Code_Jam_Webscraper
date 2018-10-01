import sys

def sortDec(x, y):
   return y - x

N = int(sys.stdin.readline())

for i in range(1, N + 1):
   line = sys.stdin.readline().strip().split()
   P = int(line[0])
   K = int(line[1])
   L = int(line[2])

   line = sys.stdin.readline().strip().split()
   freq = []
   for j in range(L):
      freq.append(int(line[j]))

   freq.sort(sortDec)
   keys = []
   for j in range(K):
      keys.append(0)


   ka = 0
   pa = 0
   answer = 0
   for j in freq:
      keys[ka] += 1
      answer += keys[ka] * j
      ka += 1
      if ka == K:
         ka = 0
      if keys[ka] > pa:
         pa = keys[ka]
         if pa > P:
            answer = -1
            break


   if answer >= 0:
      print "Case #%d: %d" %(i, answer)
   else:
      print "Case #%d: impossible" %(i)

      

