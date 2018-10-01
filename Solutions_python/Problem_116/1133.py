import sys
import math
if __name__ == "__main__":
	T = int(sys.stdin.readline().strip())
	for caseno in xrange(T):
		a = []
		b = ['X','O']
		for i in xrange(4):
			a.append(sys.stdin.readline().strip())
		win = False
		winplayer = 0
		Break = False
		for i in xrange(len(b)):
			for j in xrange(4):
				#print a[j]
				#print b[i]
				win = all((x==b[i] or x=='T') and x!='.' and x!=b[(i+1)%len(b)] for x in a[j])
				#print j, " ", win
				if win:
					winplayer = i
					Break = True
					break
			if Break:
				break
			for j in xrange(4):
				col = [c[j] for c in a]
				#print col
				win = all((x==b[i] or x=='T') and x!='.' and x!=b[(i+1)%len(b)] for x in col)
                                #print j, " ", win
                                if win:
                                        winplayer = i
                                        Break = True
                                        break
                        if Break:
                                break
			
			diag = [a[k][k] for k in range(4)]
			diag1 = ''.join(diag)
                        #print diag1
                        diag = [a[4-1-k][k] for k in range(4-1,-1,-1)]
			diag2 = ''.join(diag)
                        #print diag2
			#print b[i]
                        win = all((x==b[i] or x=='T') and x!='.' and x!=b[(i+1)%len(b)] for x in diag1)
			if win:
                        	winplayer = i
				#print "diag1 - i: ",i,"win: ", win
                                break
			win = all((x==b[i] or x=='T') and x!='.' and x!=b[(i+1)%len(b)] for x in diag2)
                        if win:
                                winplayer = i
				#print "diag2 - i: ",i,"win: ", win
                                break
		dot = False
		for i in xrange(4):
			for  j in xrange(4):
				if a[i][j] == '.':
					dot = True
					break
		if win:
			result = b[winplayer] + " won"
		elif dot:
			result = "Game has not completed"
		else:
			result = "Draw"
		print "Case #%d: %s" % (caseno + 1, result)
		sys.stdin.readline()
