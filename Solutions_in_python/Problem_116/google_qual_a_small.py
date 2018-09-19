f = open('tictac', 'r')
lines = f.readlines()
cases = lines[0]
cases = int(cases[:-1])
init=1
for case in range(cases):
   potential=1
   board=[lines[init][:-1],lines[init+1][:-1],lines[init+2][:-1],lines[init+3][:-1]]
#Draw potential check
   for i in range(len(board)):
      for j in board[i]:
         if j=='.':
            potential=0
#Substitute T's
   xboard = list(board)
   yboard = list(board)
   for a in range(len(xboard)):
      for letter in range(len(xboard[a])):
         if xboard[a][letter]=='T':
            xboard[a]=xboard[a][:letter]+'X'+xboard[a][letter+1:]
   for a in range(len(yboard)):
      for letter in range(len(yboard[a])):
         if yboard[a][letter]=='T':
            yboard[a]=yboard[a][:letter]+'O'+yboard[a][letter+1:]
#Check if X won
   xwon=0
   for row in xboard:
      if row[1]=='X' and row[2]=='X' and row[3]=='X' and row[0]=='X':
         xwon=1
   for i in range(4):
      if xboard[1][i]=='X':
         if xboard[2][i]=='X':
            if xboard[0][i]=='X' and xboard[3][i]=='X':
               xwon=1
   if xboard[1][1]=='X' and xboard[2][2]=='X':
      if xboard[0][0]=='X' and xboard[3][3]=='X':
         xwon=1
   if xboard[1][2]=='X' and xboard[2][1]=='X':
      if xboard[3][0]=='X' and xboard[0][3]=='X':
         xwon=1
   ywon=0
   for row in yboard:
      if row[1]=='O':
         if row[2]=='O':
            if row[0]=='O' and row[3]=='O':
               ywon=1
   for i in range(4):  
      if yboard[1][i]=='O':
         if yboard[2][i]=='O':
            if yboard[0][i]=='O' and yboard[3][i]=='O':
               ywon=1
   if yboard[1][1]=='O' and yboard[2][2]=='O':
      if yboard[0][0]=='O' and yboard[3][3]=='O':
         ywon=1
   if yboard[1][2]=='O' and yboard[2][1]=='O':
      if yboard[3][0]=='O' and yboard[0][3]=='O':
         ywon=1
   if xwon:
      var='X won'
   elif ywon:
      var='O won'
   elif potential:
      var='Draw'
   else:
      var='Game has not completed'
   if xwon==1 and ywon==1:
      var='Draw'

   print 'Case #'+str(case+1)+': '+var
   init=init+5
   
