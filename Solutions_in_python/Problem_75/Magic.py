def magic(line):
  l = line.split(" ")
  c = int(l[0])
  i = 1
  cDict = {}
  while(i<c+1):
    cStr = l[i]
    cDict[cStr[0:2]]=cStr[2]
    i = i + 1 

  d = int(l[i])
  idx = d + i
  i = i + 1
  dDict = {}
  while(i<=idx):
    dStr = l[i]
    dDict[dStr] = dStr
    i = i + 1

  n = int(l[i])
  fStr = l[i+1]
  #print fStr + " " + str(n) + "\n"
  j=0

  baseDict = {'Q':0, 'W':0, 'E':0, 'R':0, 'A':0, 'S':0, 'D':0, 'F':0}
  while(j<n):
    #print str(j) + " " + str(n) + " " + fStr + "\n"
    if(j==n):
      break
  
    if(baseDict.has_key(fStr[j])):
      #print str(j) + "\n"
      baseDict[fStr[j]] = baseDict[fStr[j]] + 1
    #judge last two
    if(j-1>=0):
      endPair = fStr[j-1:j+1]
      endPair_r = endPair[1]+endPair[0]
      for key in cDict.keys():
        if(key == endPair or key == endPair_r):
          baseDict[fStr[j]] = baseDict[fStr[j]] - 1
          baseDict[fStr[j-1]] = baseDict[fStr[j-1]] - 1
          fStr = fStr[0:j-1]+cDict[key]+fStr[j+1:]
          #continue
          j = j - 1
          n = len(fStr)
          break

    for dkey in dDict.keys():
      if(dkey[0]!=dkey[1]):
        if(baseDict[dkey[0]] >= 1 and baseDict[dkey[1]] >= 1 ): 
          #clear the current list
          fStr = fStr[j+1:]
          j=-1
          n = len(fStr)
          baseDict = {'Q':0, 'W':0, 'E':0, 'R':0, 'A':0, 'S':0, 'D':0, 'F':0}
          break
      else:
        if(baseDict[dkey[0]]>=2):
          #clear the current list
          fStr = fStr[j+1:]
          n = len(fStr)
          j=-1
          baseDict = {'Q':0, 'W':0, 'E':0, 'R':0, 'A':0, 'S':0, 'D':0, 'F':0}
          break
    j = j + 1
    
  id = 0
  rstStr = '['
  while(id<len(fStr)):
    rstStr = rstStr + fStr[id]
    if(id!=len(fStr)-1):
      rstStr = rstStr + ', '
    id = id + 1

  return rstStr + ']'

    

   

