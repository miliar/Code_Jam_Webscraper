def minimumFlips(pancakeString, flipperSize):
  total = 0
  pancakeArray = [1 if c == '+' else 0 for c in pancakeString]
  for index in xrange(len(pancakeString) - flipperSize + 1):
    if pancakeArray[index] != 1:
      for index2 in xrange(index, index + flipperSize):
        pancakeArray[index2] = 1 - pancakeArray[index2]
      total += 1
  for index in xrange(len(pancakeString) - flipperSize + 1, len(pancakeString)):
    if pancakeArray[index] != 1:
      return 'IMPOSSIBLE'
  return total

with open('../inputs/A-large.in') as infile:
  with open('../outputs/A-large.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      [pancakeString, flipperSize] = infile.readline().strip().split(' ')
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write(str(minimumFlips(pancakeString, int(flipperSize))))
      outfile.write('\n')
