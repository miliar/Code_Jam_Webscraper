
test = False
input =  open("Qualification/B-large.in")
output = open("Qualification/B-large.out", 'w')

def IsPossible(lawn):
  maxRow = [max(lawn[n]) for n in range(N)]
  maxCol = []
  for m in range(M):
    maxCol.append(max([lawn[x][m] for x in range(N)]))

  for n in range(N):
    for m in range(M):
      if lawn[n][m] < maxRow[n] and lawn[n][m] < maxCol[m]:
        return "NO"
  return "YES"


T = int(input.readline())
for t in range(T):
  print "case",t
  N, M = map(int, input.readline()[:-1].split(" "))
  lawn = []
  for n in range(N):
    line = input.readline()[:-1]
    lawn.append(map(int, line.split(" ")))

  result = IsPossible(lawn)

  if test == False:
    output.write("Case #{0}: {1}\n".format(t+1, result))

input.close()
if test == False:
  output.flush()
  output.close()

