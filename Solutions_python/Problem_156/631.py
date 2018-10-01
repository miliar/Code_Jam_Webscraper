def minutes(plates):
   heighest = 1
   best = 99999
   while(heighest <= max(plates)):
      mins = 0
      for s in plates:
         mins+= minsToMaxOf(s,heighest)
      mins += heighest
      if mins < best:
         best = mins
      heighest+=1
   return best
   
def minsToMaxOf(stack, max):
   return (stack-1)//max

file = open('B-large.in', 'r')
out = open('outputB.txt', 'w')
num = int(file.readline().strip())

for i in range(num):
   d = int(file.readline().strip())
   p = file.readline().strip().split(' ')
   if p:
      p = list(map(int, p))
   out.write('Case #'+str(i+1)+': ' + str(minutes(p)) + '\n')

file.close()