T = input()

for i in range(T):
  firstList, secondList = [], []

  firstAnswer = input()

  for j in range(4): firstList.append([int(x) for x in raw_input().split()])

  secondAnswer = input()

  for j in range(4): secondList.append([int(x) for x in raw_input().split()])

  commonSet = list(set(firstList[firstAnswer-1]) & set(secondList[secondAnswer-1]))

  if len(commonSet) == 0: print "Case #%d: Volunteer cheated!" % (i+1)
  if len(commonSet) == 1: print "Case #%d: %d" % (i+1, commonSet[0])
  if len(commonSet) > 1: print "Case #%d: Bad magician!" % (i+1) 