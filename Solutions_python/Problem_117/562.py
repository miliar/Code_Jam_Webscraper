def solve(fIn):
  l = {}
  rm = {}
  cm = {}
  line = fIn.readline()
  [N, M] = [int(x) for x in line.split()]

  for i in range(N):
    line = fIn.readline()
    l[i] = [int(x) for x in line.split()]
    rm[i] = max(l[i])

  for j in range(M):
    cm[j] = 0
    for i in range(N):
      cm[j] = max(cm[j], l[i][j])

  result = 'YES'
  for i in range(N):
    for j in range(M):
      if not (rm[i] <= l[i][j] or cm[j] <= l[i][j]):
        result = 'NO'
        break
    if result == 'NO':
      break;

  return result

def main(filename):
  fIn = open(filename)
  fOut = open(filename+'.out', 'w')
  numTestCases=int(fIn.readline())
  for i in range(numTestCases):
    result = solve(fIn)
    fOut.write('Case #' + str(i+1) + ': ' + result + '\n')

  fIn.close()
  fOut.close()
  return
    

main('D:\\tech\\code_jam\\2013\\Problem B. Lawnmower\\B-large.in')


