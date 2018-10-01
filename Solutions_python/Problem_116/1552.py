# Tic-Tac-Toe-Tomek

import sys

class LoopContinue(Exception):
	pass

with open(sys.argv[1], 'r') as f:
	n = int(f.readline().strip())

	for i in xrange(n):
		# Read in 4 lines and then an empty line
		L1 = f.readline().strip()
		L2 = f.readline().strip()
		L3 = f.readline().strip()
		L4 = f.readline().strip()
		f.readline()

		# Compute two versions of matrix, one where T->X and one where T->O
		MX = [list(L1.replace('T', 'X')), list(L2.replace('T', 'X')), list(L3.replace('T', 'X')), list(L4.replace('T', 'X'))]
		MXT = zip(*MX)
		MXD = [MX[0][0], MX[1][1], MX[2][2], MX[3][3]]
		MXDP = [MX[0][3], MX[1][2], MX[2][1], MX[3][0]]
		MO = [list(L1.replace('T', 'O')), list(L2.replace('T', 'O')), list(L3.replace('T', 'O')), list(L4.replace('T', 'O'))]
		MOT = zip(*MO)
		MOD = [MO[0][0], MO[1][1], MO[2][2], MO[3][3]]
		MODP = [MO[0][3], MO[1][2], MX[2][1], MO[3][0]]
		T = L1 + L2 + L3 + L4

		# Check for a win condition
		try:
			for r in range(4):
				if ''.join(MX[r]) == "XXXX" or ''.join(MXT[r]) == "XXXX":
					print "Case #%d: X won" % (i+1)
					raise LoopContinue
				elif ''.join(MO[r]) == "OOOO" or ''.join(MOT[r]) == "OOOO":
					print "Case #%d: O won" % (i+1)
					raise LoopContinue
			if ''.join(MXD) == "XXXX" or ''.join(MXDP) == "XXXX":
				print "Case #%d: X won" % (i+1)
				raise LoopContinue
			elif ''.join(MOD) == "OOOO" or ''.join(MODP) == "OOOO":
				print "Case #%d: O won" % (i+1)
				raise LoopContinue

			# Check for a draw condition (not win, but no empty)
			if '.' not in T:
				print "Case #%d: Draw" % (i+1)
			else:
				print "Case #%d: Game has not completed" % (i+1)
		except LoopContinue:
			continue