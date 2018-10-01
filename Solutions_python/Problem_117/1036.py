import math
import sys

# esta buen
def canCut(lawn, h, row = None, col = None):
	if row != None:
		trace("Testing cut of row %i"%row)
		for i in range(len(lawn[row])):
			if lawn[row][i] > h:
				trace(False)
				return False
		trace(True)
		return True

	if col != None:
		trace("Testing cut of col %i"%col)
		for i in range(len(lawn)):
			if lawn[i][col] > h:
				trace(False)
				return False
		trace(True)
		return True
	raise "Error: No se especifico fila ni columna"


def cut(lawn, h, row = None, col = None):
	if row != None:
		trace(row, "Cortando fila a (h: %s)"%h)
		for i in range(len(lawn[row])):
			lawn[row][i] = h
				
		return

	if col != None:
		trace(col, "Cortando columna a (h: %s): "%h)
		for i in range(len(lawn)):
			lawn[i][col] = h
		return
	raise "Error: No se especifico fila ni columna"


def isLawnPosible2(lawn, m, n):
	l = []
	for i in lawn:
		l = l + i
	h = sorted(set(l), reverse = True) 
	lawn_copy = x = [[ h[0] for i in range(n)] for j in range(m)]
	#trace([m, n], "dimensiones")
	#trace(lawn_copy, "lawn_copy_before")
	#trace(lawn, "lawn...")
	# para cada una de las alturas
	for height in h:
		# las esquinas
		corners=[[0, 0], [m-1, 0], [m-1, n-1], [0, n-1]]
		for c in corners:
			cellh = lawn[c[0]][c[1]]
			if cellh == height:
				opositeRow = m-1 if c[0] == 0 else 0
				opositeCol = n-1 if c[1] == 0 else 0

				if m > 1:
					if cellh >= lawn[c[0]][opositeCol]:
						if not canCut(lawn, cellh, row=c[0]):
							trace(c, "No puede por fila")
							return "NO" 
						# cortar fila c[0]
						cut(lawn_copy, cellh, row = c[0])


				if n > 1:
					if cellh >= lawn[opositeRow][c[1]]:
						if not canCut(lawn, cellh, col=c[1])  :
							trace(c, "No puede por columna")
							return "NO"
						# cortar columna c[1]
						cut(lawn_copy, cellh, col = c[1])
					


		# recorre las filas (sin las esquinas)
		for i in range(1, m-1):
			if lawn[i][0] == height:
				trace(canCut(lawn, height, row = i), "can cut row %i"%i)
				if canCut(lawn, height, row = i):
					cut(lawn_copy, height, row = i)
				#else:
				#	if m > 1:
				#		trace(i, "no se puede cortar fila ")
				#		return "NO"

		for j in range(1, n-1):
			if lawn[0][j] == height:
				if canCut(lawn, height, col = j):
					cut(lawn_copy, height, col = j)
				#else:
				#	if n > 1:
				#		trace(j, "no se puede cortar columna ")
				#		return "NO"

	#trace(lawn_copy, "lawn_copy_after")
	if lawn == lawn_copy:
		return "YES"
	else:
		trace([lawn, lawn_copy],"No quedan iguales ")
		return "NO"




def isLawnPosible(lawn, m, n):
	l = []
	for i in lawn:
		l = l + i
	heights = sorted(set(l), reverse = True) 
	lawn_copy = x = [[ heights[0] for i in range(n)] for j in range(m)]

	# para cada altura
	for h in heights:
		# intenta cortar por fila
		for i in range(0, m):
			if canCut(lawn, h, row = i):
				cut(lawn_copy, h, row = i)

		for j in range(0, n):
			if canCut(lawn, h, col = j):
				cut(lawn_copy, h, col = j)

	if lawn == lawn_copy:
		return "YES"
	else:
		trace([lawn, lawn_copy],"No quedan iguales ")
		return "NO"



def main():
	inputFolder = "/home/pabratte/Downloads/"
	input = open(inputFolder+sys.argv[1])
	nTestCases = int(input.readline())
	for i in range(0, nTestCases):
		[m, n] = [int(s) for s in input.readline().split() if s.isdigit()]
		
		lawn = [[int(s) for s in input.readline().split() if s.isdigit()]]
		for j in range(1, m):
			lawn.append([int(s) for s in input.readline().split() if s.isdigit()])
		print "Case #%i: %s"%(i+1, isLawnPosible(lawn, m, n))


	input.close()

def trace(var, msg = ""):
	return
	print "-- "+str(msg)+" "+str(var)

if __name__ == "__main__":
    main()
