f = open('input6.txt')


def solve(armin, motes, depth = 0):
  total = armin
  index = 0

  if total == 1:
    return len(motes)

  for i,mote in enumerate(motes):
    if mote < total:
      total += mote
      index += 1
    else:
      index -= 1
      index = max(index, 0)
      break

  # print armin,total, motes, index
  if index == len(motes):
    return 0
  else:
    kick = total - 1
    ml = len(motes[index:])
    mmotes = motes[0:len(motes)-1]

    motes.append(kick)
    motes.sort()

    #arbitrary limit to stop infinite recursion
    if depth > 50:
      return 0
    return min(1 + solve(armin, motes, depth+1), 1 + solve(armin, mmotes, depth+1),ml)
  


def main():
  numInputs = int(f.readline())

  for i in range(numInputs):
    line1 = f.readline().split(' ')
    line2 = f.readline().split(' ')

    armin = int(line1[0])
    motes = map(int, line2)
    motes.sort()

    ans = solve(armin, motes)
    print 'Case #{0}: {1}'.format(i+1, ans)

main()