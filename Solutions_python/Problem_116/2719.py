
def analyze(game,k):
	#checking for a win
	#principal diagonal
	a=set()
	for i in range(4):
		a.add(game[i][i])
	if a.issubset({"X","T"}) :
		return "Case #"+str(k)+": X won"
	elif a.issubset({"O","T"}):
		return "Case #"+str(k)+": O won"
	#second diagonal
	a=set()
	for i in range(4):
		a.add(game[i][3-i])
	if a.issubset({"X","T"}):
		return "Case #"+str(k)+": X won"
	elif a.issubset({"O","T"}):
		return "Case #"+str(k)+": O won"
	for i in range(4):
		#horizontal
		a=set()
		for j in range(4):
			a.add(game[i][j])
		if a.issubset({"X","T"}):
			return "Case #"+str(k)+": X won"
		elif a.issubset({"O","T"}):
			return "Case #"+str(k)+": O won"
		#vertical
		a=set()
		for j in range(4):
			a.add(game[j][i])
		if a.issubset({"X","T"}):
			return "Case #"+str(k)+": X won"
		elif a.issubset({"O","T"}):
			return "Case #"+str(k)+": O won"
	#checking for a draw
	#principal diagonal
	a=set()
	for i in range(4):
		a.add(game[i][i])
	if not {"X","O"}.issubset(a):
		return "Case #"+str(k)+": Game has not completed"
	#second diagonal
	a=set()
	for i in range(4):
		a.add(game[i][3-i])
	if not {"X","O"}.issubset(a):
		return "Case #"+str(k)+": Game has not completed"
	for i in range(4):
		#horizontal
		a=set()
		for j in range(4):
			a.add(game[i][j])
		if not {"X","O"}.issubset(a):
			return "Case #"+str(k)+": Game has not completed"
		#vertical
		a=set()
		for j in range(4):
			a.add(game[j][i])
		if not {"X","O"}.issubset(a):
			return "Case #"+str(k)+": Game has not completed"
	return "Case #"+str(k)+": Draw"
		
f=open("text.dat")
T=f.readline()
for j in range(int(T)):
	game=[]
	for i in range(4):
		game.append(list(f.readline())[0:-1])
	f.readline()
	print analyze(game,j+1)
