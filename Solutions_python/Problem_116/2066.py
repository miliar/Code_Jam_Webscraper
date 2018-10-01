#!/usr/bin/python -tt

def getO(lst):
 b = ''
 for i in range(4):
  for j in range(4):
   if lst[i][j]== 'O':
    op = (i,j)
    b = checkO(op,lst)
   if b == 'O': return 'O'
 return None
 
def checkO(lst):
 x = 0
 y = 0
 if ((lst[x][y]=='O' or (lst[x][y]=='T'))&(lst[x+1][y+1]=='O' or (lst[x+1][y+1]=='T'))&(lst[x+2][y+2]=='O' or (lst[x+2][y+2]=='T')) and ((lst[x+3][y+3]=='O') or lst[x+3][y+3]=='T') ): return 'O'
 x = 3
 y = 0
 if ((lst[x][y]=='O' or (lst[x][y]=='T'))&(lst[x-1][y+1]=='O' or (lst[x-1][y+1]=='T'))&(lst[x-2][y+2]=='O' or (lst[x-2][y+2]=='T')) and ((lst[x-3][y+3]=='O') or lst[x-3][y+3]=='T' ) ): return 'O'

 x = 0
 for y in range(4):
  if ((lst[x][y]=='O' or (lst[x][y]=='T'))&(lst[x+1][y]=='O' or (lst[x+1][y]=='T'))&(lst[x+2][y]=='O' or (lst[x+2][y]=='T')) and ((lst[x+3][y]=='O') or lst[x+3][y]=='T')): return 'O'
 y = 0
 for x in range(4):
  if ((lst[x][y]=='O' or (lst[x][y]=='T'))&(lst[x][y+1]=='O' or (lst[x][y+1]=='T'))&(lst[x][y+2]=='O' or (lst[x][y+2]=='T'))and ((lst[x][y+3]=='O') or lst[x][y+3]=='T')): return 'O'

 return ''



def checkX(lst):
 x = 0
 y = 0
 if ((lst[x][y]=='X' or (lst[x][y]=='T'))&(lst[x+1][y+1]=='X' or (lst[x+1][y+1]=='T'))&(lst[x+2][y+2]=='X' or (lst[x+2][y+2]=='T')) and ((lst[x+3][y+3]=='X') or lst[x+3][y+3]=='T') ): return 'X'
 x = 3
 y = 0
 if ((lst[x][y]=='X' or (lst[x][y]=='T'))&(lst[x-1][y+1]=='X' or (lst[x-1][y+1]=='T'))&(lst[x-2][y+2]=='X' or (lst[x-2][y+2]=='T')) and ((lst[x-3][y+3]=='X') or lst[x-3][y+3]=='T' ) ): return 'X'

 x = 0
 for y in range(4):
  if ((lst[x][y]=='X' or (lst[x][y]=='T'))&(lst[x+1][y]=='X' or (lst[x+1][y]=='T'))&(lst[x+2][y]=='X' or (lst[x+2][y]=='T')) and ((lst[x+3][y]=='X') or lst[x+3][y]=='T')): return 'X'
 y = 0
 for x in range(4):
  if ((lst[x][y]=='X' or (lst[x][y]=='T'))&(lst[x][y+1]=='X' or (lst[x][y+1]=='T'))&(lst[x][y+2]=='X' or (lst[x][y+2]=='T'))and ((lst[x][y+3]=='X') or lst[x][y+3]=='T')): return 'X'

 return ''



def ifT(lst):
 for i in range(4):
  for j in range(4):
   if lst[i][j] == 'T': return True
 return False

a = raw_input()
result =''
count = 0
for i in range(int(a)):
 p =''
 count +=1
 lst = ['','','','']
 for j in range(4):
  lst[j] = raw_input()
 result = raw_input()
 op = None
 O=0
 X = 0
 for i in range(4):
  for j in range(4):
   if lst[i][j]=='O':O+=1
   if lst[i][j]=='X':X+=1 

 result = checkO(lst)
 if result == '': result = checkX(lst)

 if result == '':
  p = 'Draw' 
  for i in range(4):
   for j in range(4):
    if lst[i][j] == '.':
     p = 'Game has not completed'
  print 'Case #'+str(count)+': '+p

 else :
  p = result+' won'
  print 'Case #'+str(count)+': '+p

