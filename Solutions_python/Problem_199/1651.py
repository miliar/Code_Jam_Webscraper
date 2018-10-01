testNum = int(input())
testCount =0
def flip(pancakes, index, flipper):
   counter = index
   while counter < (index+flipper):
      if pancakes[counter] == "-":
         pancakes[counter] = "+"
      else:
         pancakes[counter] = "-"
      counter +=1
while testCount < testNum:
   line = input()
   line = line.split()
   flipper = int(line[1])
   line.remove(str(flipper))
   pancakes = line[0]
   pancakes = list(pancakes)
   flips = 0
   counter = 0
   if(flipper> len(pancakes)):
      print("Case #{:d}: {:s}".format(testCount+1,"IMPOSSIBLE"))
      continue
   while counter < len(pancakes):
      if pancakes[counter] == "-":
         flip(pancakes, counter, flipper)
         flips+=1
      if "-" not in pancakes:
         print("Case #{:d}: {:d}".format(testCount+1,flips))
         break
      if counter == len(pancakes)-flipper:
         print("Case #{:d}: {:s}".format(testCount+1,"IMPOSSIBLE"))
         break
      counter+=1
   testCount +=1

   