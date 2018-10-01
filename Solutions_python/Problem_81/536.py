import os
import array

def wp(player, mat):
	wins = 0.0
	games = 0.0
	for ch in mat[player]:
		if (ch == '1'):
			wins = wins + 1
			games = games + 1
		if (ch == '0'):
			games = games + 1
	return wins / games
	
def owp(player, mat):
	l = []
	for i in range(len(mat[player])):
		if (mat[player][i] != '.'):
			l.append(wpwithout(i, player, mat))
	
	sum = 0
	for w in l:
		sum = sum + w
	return sum / len(l)
	
def oowp(player, mat):
	l = []
	for i in range(len(mat[player])):
		if (mat[player][i] != '.'):
			l.append(owp(i, mat))
	
	sum = 0
	for w in l:
		sum = sum + w
	return sum / len(l)
	

def wpwithout(player, player2, mat):
	wins = 0.0
	games = 0.0
	for i in range(len(mat[player])):
		if (i != player2):
			if (mat[player][i] == '1'):
				wins = wins + 1
				games = games + 1
			if (mat[player][i] == '0'):
				games = games + 1
	return wins / games

f = open("A-small-attempt0.in",'r');
g = open("results1.dat",'w')
n = int(f.readline())


for l in range(n):

	m = int(f.readline())
	
	mat = []
	for i in range(m):
		mat.append(list(f.readline().rstrip()))
	
	#print mat
	
#	for player in range(m):
		#print wp(player, mat)
		#print owp(player, mat)
		#print oowp(player, mat)
	#	print 0.25 * wp(player, mat) + 0.5 * owp(player, mat) + 0.25 * oowp(player, mat)

	g.write("Case #" + repr(l+1) + ":\n")
	for player in range(m):
		#print wp(player, mat)
		#print owp(player, mat)
		#print oowp(player, mat)
		g.write(repr(0.25 * wp(player, mat) + 0.5 * owp(player, mat) + 0.25 * oowp(player, mat))+"\n")
	
	
f.close()
g.close()





