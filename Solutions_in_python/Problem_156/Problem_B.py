import string, math

# _file = open("./B-large.in")
_file = open("./B-small-attempt2.in")
_result = open("./result.txt", "w")

datasetSize = int(_file.readline())

for i in range(datasetSize):
  dinnersCount = int(_file.readline().replace("\n", ""))
  dinnersPancakes = [int(number) for number in _file.readline().replace("\n", "").split(' ')]

  # Sort and invert (first will be biggest)
  dinnersPancakes.sort()
  dinnersPancakes.reverse()

  # Create a list of tupples (number, number of occurences)
  tupledPancakes = list()
  for pancakeIndex, pancake in enumerate(dinnersPancakes):
    if len(tupledPancakes) > 0 and tupledPancakes[-1][0] == pancake:
      tupledPancakes[-1] = (pancake, tupledPancakes[-1][1] + 1)
    else:
      tupledPancakes.append((pancake, 1))

  # By default min will be to just wait all the time
  minMinutes = tupledPancakes[0][0]

  # print dinnersCount, dinnersPancakes, tupledPancakes

  # Try to split only first, then first 2, then first 3
  for splitCount in range(1, len(tupledPancakes) + 1):
    totalSplitCount = sum(cake[1] for cake in tupledPancakes[0:splitCount])

    biggestNonSplited = 0
    if splitCount < len(tupledPancakes):
      biggestNonSplited = tupledPancakes[splitCount][0]

    # Number of splits
    for splitTimes in range(1, minMinutes - biggestNonSplited + 1, 1):

      # Number of splits should be at least as big as number of numbers to be split
      # if splitCount > splitTimes:
      if totalSplitCount > splitTimes:
        continue

      # What's the smallest possible biggest division result
      # Each number that should be split will receive at least 1 division point
      # all the others will be distributed based on number weight
      numbersWeight = sum((cake[0] * cake[1]) for cake in tupledPancakes[0:splitCount])
      divisionsToShare = splitTimes - totalSplitCount
      oneCakeDivisionsShare = 1.0 * divisionsToShare / numbersWeight

      # print numbersWeight, divisionsToShare, oneCakeDivisionsShare

      # Find max necessary minutes to process cackes
      maxMinutes = biggestNonSplited + splitTimes

      for cake in tupledPancakes[0:splitCount]:
        hasDivisions = round(cake[0] * cake[1] * oneCakeDivisionsShare)
        additionalDivisions = hasDivisions // cake[1]
        # print 'c', hasDivisions, cake, additionalDivisions

        divideBy = 2.0 + additionalDivisions # will be float
        smallCakeSize = math.ceil(cake[0]/divideBy) # will be float

        maxMinutes = max(maxMinutes, int(smallCakeSize + splitTimes))

      # Check if maxMinutes is smaller than minMinutes
      minMinutes = min(minMinutes, maxMinutes)

      # print "split numbers " + str(splitCount) + " split times " + str(splitTimes) + " weight " + str(numbersWeight) + " time " + str(maxMinutes)

  result = "Case #" + str(i + 1) + ": " + str(minMinutes)

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
