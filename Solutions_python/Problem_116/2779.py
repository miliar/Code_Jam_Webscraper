import sys

def checkRow(matrix,m,n):
  cont = 0
  if n == 3:
    n =2
  for i in range(4):
    if matrix[m][i] == matrix[m][n]: 
      cont +=1
  if cont == 3: return matrix[m][n] 
  return False


def checkDia(matrix,m,n):
  l = len(matrix)
  lr= [matrix[i][i] for i in range(l)]              # [-2, -6, 7,  8]
  rl= [matrix[l-1-i][i] for i in range(l-1,-1,-1)]  # [ 2,  5, 2, -1]
  cnt = 0
  cnt2 = 0
  for XO in lr:
    if XO == lr[3]:
      cnt+=1
  if cnt == 4:
    return lr[3]
  for XO in rl:
    if XO == rl[3]:
      cnt2+=1
  if cnt2 == 4:
    return rl[3]
  
  cnt,cnt2 =0,0
  if 'T' in lr:
    lr.pop(lr.index('T'))
    for XO in lr:
      if XO == lr[2]:
        cnt+=1
    if cnt == 3:
      return lr[2]
  if 'T' in rl:
    rl.pop(rl.index('T'))
    for XO in rl:
      if XO == rl[2]:
        cnt2+=1
    if cnt2 == 3:
      return rl[2]
  return None


def checkCol(matrix):
  DA = checkDia(matrix,0,0)
  if DA:
    return DA 
  for m in range(4):
    cnt = 0
    for n in range(4):
      if matrix[m][n] == 'T':
        TTT = checkRow(matrix,m,n)
        if not TTT:
          DIA = checkDia(matrix,m,n)
          if DIA:
            return DIA
          return None
        return TTT
      if matrix[m][n] == '.':
        continue
      if matrix[m][n] == matrix[m][3]:
          cnt = cnt+1
          if cnt ==4:
            return matrix[m][3]
  return None


def vertical(rl):
    cnt2 = 0
    rl.pop(rl.index('T'))
    for XO in rl:
      if XO == rl[2]:
        cnt2+=1
    if cnt2 == 3:
      return rl[2]
    return None
 
 
def chkColm(matrix):
  cnt = 0
  for m in range(4):
    cnt = 0
    for n in range(4):
      if matrix[n][m] == '.':
        continue
      if matrix[n][m] == 'T':
        VER = vertical([row[m] for row in matrix])
        if VER:
          return VER
      if matrix[n][m] == matrix[3][m]:
        cnt+=1
        if cnt == 4:
          return matrix[3][m]
  return False
#      return checkRow(line,line.pop(line.index('T'))): 



if __name__ == '__main__':
    fileHandle = open(sys.argv[1])
    lines = fileHandle.readlines()
    totallines = int(lines.pop(0).rstrip())
    matrix = {}
    j = 0
    result= {
    'X': "X won",
    'O': "O won",
    '.': "Game has not completed",
    'D': "Draw"
    }
    for i in range(0, 5*totallines, 5):
      j = j+1
      one_m = []
      if i != 4:
        for k in range(4):
			    one_m.append([x for x in lines[i+k].rstrip()])
   
      matrix[j] = one_m
    for ad,mat in matrix.iteritems():
      RES = checkCol(mat)
      if not RES:
        RES = chkColm(mat)
      if not RES:
        RES = 'D' 
      print 'Case #%s: %s' % (ad, result[RES])
