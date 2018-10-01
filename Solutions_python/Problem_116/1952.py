
def check_win(board,sym):
     for i in xrange(4):
	  won=True
	  for j in xrange(4):
	       if board[i][j]!=sym and board[i][j]!='T':
		    won=False
		    break
	  if won:
	       return True
	  
	  won=True     
	  for j in xrange(4):
	       if board[j][i]!=sym and board[j][i]!='T':
		    won=False
		    break
		    
	  if won:
	       return True

     won=True
     for i in xrange(4):
	  if board[i][i]!=sym and board[i][i]!='T':
	       won=False
	       break
     if won:
	  return True
	  
     won=True
     for i in xrange(4):
	  if board[i][3-i]!=sym and board[i][3-i]!='T':
	       won=False
	       break
     
     return won

def check_empty(board):
     for row in board:
	  if '.' in row: return True

for t in xrange(int(raw_input())):
     board=[]
     
     for j in xrange(4):
	  board.append(raw_input().strip())
     if check_win(board, 'X'):
	   print "Case #"+str(t+1)+": X won"
	   
     elif check_win(board, 'O'):
	   print "Case #"+str(t+1)+": O won"
     
     elif check_empty(board):
	   print "Case #"+str(t+1)+": Game has not completed"
     else:
	   print "Case #"+str(t+1)+": Draw"
     temp=raw_input()
	       