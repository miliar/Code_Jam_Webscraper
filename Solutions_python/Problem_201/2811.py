import sys

# if say, 4 stalls and 2
# people, then:
#  o s s s s o
#    0 1 2 3
#    3 2 1 0

# calc max of min(l,r)
# this gives the two centre
# then as two, choose max of
# max(l,r)
# this also gives two, so choose
# the left most
#  o s o s s o
#    0   0 1
#    0   1 0

# so as total people
# is 2, the last person chooses
# L=0, R=1
# y = max(l,r) = 1
# z = min(l,r) = 0

# (if there were more people)
# same deal, choose left
#  o s o o s o
#    0     0
#    0     0

# choose left, so

#  o o o o s o
#          0
#          0

# both middle stalls will be taken
# so the user choses stall 0 (first)
# this has L=0, and R=


def calcLeftmost(index, stallArray):
  stalls = stallArray[:]
  if(stalls[index] == 1):
    return -1
  i = index
  count = 0
  while(i-1 >= 0 and stalls[i-1] != 1):
    count += 1
    i -=1

  return count


def calcRighmost(index, stallArray):
  stalls = stallArray[:]
  if(stalls[index] == 1):
    return -1
  i = index
  count = 0
  while(i+1 < len(stalls) and stalls[i+1] != 1):
    count += 1
    i +=1

  return count

def getMinOfMax(stallArray, lArray, rArray):
  stalls = stallArray[:]
  L = lArray[:]
  R = rArray[:]
  duplicates = []
  minId = 0
  maxVal = 0
  for i in range(1, len(stalls)-1):
    if(stalls[i] == 1):
      continue
    minVal = min(L[i], R[i])
    if(minVal > maxVal or (minVal==maxVal and minId==0)):
      maxVal = minVal
      minId = i
      duplicates = []
    elif(minVal == maxVal):
      duplicates.append(i)


  if(len(duplicates) > 0):
    idList = duplicates[:]
    idList.append(minId)
    minId = getMaxOfMax(stalls, L, R, idList)


  return minId


def getMaxOfMax(stallArray, lArray, rArray, listOfIds):
  idList = listOfIds[:]
  stalls = stallArray[:]
  L = lArray[:]
  R = rArray[:]
  secondDups = []
  maxId = 0
  mainMaxVal = 0
  for i in range(len(idList)):
    index = idList[i]
        
    maxVal = max(L[index], R[index])

    if(maxVal > mainMaxVal or (mainMaxVal==maxVal and maxId==0)):
      mainMaxVal = maxVal
      maxId = index
      secondDups = []
    elif(maxVal == mainMaxVal):
      secondDups.append(index)

  if(len(secondDups) > 0):
    return min(maxId, secondDups[0])

  return maxId


def calcStalls(numString):
  # PROGRAM START

  n = int(numString[0])
  k = int(numString[1])
  # create stalls, L, and R
  L = [-1]
  R = [-1]
  stalls = [1]
  for i in range(n):
    L.append(0)
    R.append(0)
    stalls.append(0)

  # add last guard stall
  L.append(-1)
  R.append(-1)
  stalls.append(1)
  chosenstalls = []
  for j in range(k):
    # calculate L and R values
    for i in range(1, len(stalls)-1):
      L[i] = calcLeftmost(i, stalls)
      R[i] = calcRighmost(i, stalls)


    # now choose s
    stallId = getMinOfMax(stalls, L, R)

    # if last person, save details
    if(j == k-1):
      yz = []
      yz.append(max(L[stallId], R[stallId]))
      yz.append(min(L[stallId], R[stallId]))
      return str(yz[0]) + " " + str(yz[1])

    else:
      # else, occupy and loop
      chosenstalls.append(stallId)
      stalls[stallId] = 1


def main():
  filepath = sys.argv[1]
  with open(filepath) as f:
    content = f.readlines()

  content = [x.strip() for x in content]
  for j in range(1, len(content)):
    nums = content[j].split(" ")
    result = calcStalls(nums)
    content[j] = "Case #" + str(j) + ": " + result + "\n"

  target = open("output_numbers.txt", 'w')
  for i in range(len(content)):
    line = content[i]
    if(i == 0):
     continue 
    target.write(content[i])

main()
