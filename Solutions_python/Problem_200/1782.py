testNum = int(input())
testCount =0
while testCount < testNum:
   number = input()
   numberList = str(number)
   numberList = list(numberList)
   counter = 1
   while counter < len(numberList):
      if sorted(numberList) == numberList:
         break
      if numberList[counter] < numberList[counter-1]:
         numberList[counter-1] = str(int(numberList[counter-1])-1)
         if numberList[counter-1] >= numberList[counter-2] or (counter-2 < 0):
            while counter< len(numberList):
               numberList[counter] = "9"
               counter+=1
            break
         counter = 0
      counter +=1
   print("Case #{:d}: {:d}".format(testCount+1,int("".join(numberList))))
   testCount +=1