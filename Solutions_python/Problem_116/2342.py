fileFirstlineOpen = open('small.txt', 'r+')
n = fileFirstlineOpen.readline() #read first line, number of boards in file
fileFirstlineOpen.close()

def processBoard(lines):
   linesX = []
   linesY = []
   dotsExist = False
   for index,lContents in enumerate(lines):
    if "." in lines[index]: dotsExist = True
    linesX.append(lines[index].replace("T","X").rstrip())
    linesY.append(lines[index].replace("T","O").rstrip())
   if linesX[0].count("X") == 4 or linesX[1].count("X") == 4 or linesX[2].count("X") == 4 or linesX[3].count("X") == 4: return "X won" #horizontal 
   if linesY[0].count("O") == 4 or linesY[1].count("O") == 4 or linesY[2].count("O") == 4 or linesY[3].count("O") == 4: return "O won" #horizontal

   if (linesX[0][0] == linesX[1][1] == linesX[2][2] == linesX[3][3] and linesX[0][0] == "X") or \
     (linesX[0][3] == linesX[1][2] == linesX[2][1] == linesX[3][0] and linesX[0][3] == "X") : return "X won" #diag
   if (linesY[0][0] == linesY[1][1] == linesY[2][2] == linesY[3][3] and linesY[0][0] == "O") or \
     (linesY[0][3] == linesY[1][2] == linesY[2][1] == linesY[3][0] and linesY[0][3] == "O") : return "O won" #diag
  
   if (linesX[0][0] == linesX[1][0] == linesX[2][0] == linesX[3][0] and linesX[0][0] == "X") or \
     (linesX[0][1] == linesX[1][1] == linesX[2][1] == linesX[3][1] and linesX[0][1] == "X") or \
	 (linesX[0][2] == linesX[1][2] == linesX[2][2] == linesX[3][2] and linesX[0][2] == "X") or \
	 (linesX[0][3] == linesX[1][3] == linesX[2][3] == linesX[3][3] and linesX[0][3] == "X") : return "X won" #vertical
   if (linesY[0][0] == linesY[1][0] == linesY[2][0] == linesY[3][0] and linesY[0][0] == "O") or \
     (linesY[0][1] == linesY[1][1] == linesY[2][1] == linesY[3][1] and linesY[0][1] == "O") or \
	 (linesY[0][2] == linesY[1][2] == linesY[2][2] == linesY[3][2] and linesY[0][2] == "O") or \
	 (linesY[0][3] == linesY[1][3] == linesY[2][3] == linesY[3][3] and linesY[0][3] == "O") : return "O won" #vertical
   
   if dotsExist: return "Game has not completed"
   return "Draw"

f = open('small.txt', 'r+')
o = open("output.txt","a")
lines = []
for index,lContents in enumerate(f):
 if index % 5 == 0: continue
 elif index % 5 >= 1 and index % 5 <= 3: lines.append(lContents)
 elif index % 5 == 4 :
  lines.append(lContents)
  res = "Case #"+str((index/5)+1)+": "+processBoard(lines)
  o.write(res+"\n")
  print res
  lines = []

f.close()