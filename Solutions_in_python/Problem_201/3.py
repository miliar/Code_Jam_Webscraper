# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

  stalls = [range(1, n+1)]
  while m > 0:
    minMaxVal = -1
    stallSetIndex = 0
    stallIndex = 0
    maxmaxVal = -1

    for stallSetIdx in range(len(stalls)):
      stallSet = stalls[stallSetIdx]
      midIndex = (len(stallSet)-1)/2
      tempMinVal = min(len(stallSet) - midIndex - 1, midIndex)

      if minMaxVal <= tempMinVal:
        if minMaxVal == tempMinVal:
          if maxmaxVal < max(len(stallSet) - midIndex - 1, midIndex):
            minMaxVal = tempMinVal
            stallSetIndex = stallSetIdx
            stallIndex = midIndex
            maxmaxVal = max(len(stallSet) - midIndex - 1, midIndex)
        else:
          minMaxVal = tempMinVal
          stallSetIndex = stallSetIdx
          stallIndex = midIndex
          maxmaxVal = max(len(stallSet) - midIndex - 1, midIndex)

    store = stalls[stallSetIndex][:]
    if len(store[:stallIndex]) != 0:
      stalls.append(store[:stallIndex])
    if len(store[stallIndex+1:]) != 0:
      stalls.append(store[stallIndex+1:])
    del stalls[stallSetIndex]

    m -= 1

  print "Case #{}: {} {}".format(i, maxmaxVal, minMaxVal)
