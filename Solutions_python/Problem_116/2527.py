#!/usr/bin/python
 
def fun(l):
 for i in range(4):
  if((l[0][i]=='O' or l[0][i]=='T')and (l[1][i]=='O' or l[1][i]=='T') and (l[2][i]=='O' or l[2][i]=='T') and (l[3][i]=='T' or l[3][i]=='O')):
   return 'O won'
  if((l[i][0]=='O' or l[i][0]=='T')and (l[i][1]=='O' or l[i][1]=='T') and (l[i][2]=='O' or l[i][2]=='T') and (l[i][3]=='T' or l[i][3]=='O')):
   return 'O won'
  if((l[0][0]=='O' or l[0][0]=='T')and (l[1][1]=='O' or l[1][1]=='T') and (l[2][2]=='O' or l[2][2]=='T') and (l[3][3]=='T' or l[3][3]=='O')):
   return 'O won'
  if((l[3][0]=='O' or l[3][0]=='T')and (l[2][1]=='O' or l[2][1]=='T') and (l[1][2]=='O' or l[1][2]=='T') and (l[0][3]=='T' or l[0][3]=='O')):   
   return 'O won' 
  
  if((l[0][i]=='X' or l[0][i]=='T')and (l[1][i]=='X' or l[1][i]=='T') and (l[2][i]=='X' or l[2][i]=='T') and (l[3][i]=='T' or l[3][i]=='X')):
   return 'X won'
  if((l[i][0]=='X' or l[i][0]=='T')and (l[i][1]=='X' or l[i][1]=='T') and (l[i][2]=='X' or l[i][2]=='T') and (l[i][3]=='T' or l[i][3]=='X')):
   return 'X won'
  if((l[0][0]=='X' or l[0][0]=='T')and (l[1][1]=='X' or l[1][1]=='T') and (l[2][2]=='X' or l[2][2]=='T') and (l[3][3]=='T' or l[3][3]=='X')):
   return 'X won'
  if((l[3][0]=='X' or l[3][0]=='T')and (l[2][1]=='X' or l[2][1]=='T') and (l[1][2]=='X' or l[1][2]=='T') and (l[0][3]=='T' or l[0][3]=='X')):
   return 'X won'
 
 for i in range(4):
  for j in range(4):
   if( l[i][j]=='.') : return 'Game has not completed'
 return 'Draw'  

def main():
 count=0
 total=input()
 for l in range(total):
  count+=1
  b = ['','','','']
  for j in range(4):
   b[j]=raw_input()
  t=raw_input()
  s=fun(b)
  print 'Case #'+str(count)+':',s 


if __name__ == '__main__':
 main()
