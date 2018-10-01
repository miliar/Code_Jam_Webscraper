f = open('tictac', 'r')
lines = f.readlines()
cases = lines[0]
cases = int(cases[:-1])
init=1
for i in range(cases):
   completeness=1
   board=[lines[init][:-1],lines[init+1][:-1],lines[init+2][:-1],lines[init+3][:-1]]
   print board
#Completeness check
   for i in range(len(board)):
      for j in board[i]:
         if j=='.':
            completeness=0
   print completeness
   if completeness==1:
      #X check



   init=init+5
   
