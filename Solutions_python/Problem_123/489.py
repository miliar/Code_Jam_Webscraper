from time import sleep
# ------------------------------------------------------------------------------
# globals
# ------------------------------------------------------------------------------
pi = 3.14159265
# ------------------------------------------------------------------------------
# solution
# ------------------------------------------------------------------------------

f = open('in')
fo = open('out', 'w')

for T in range(int(f.readline())):
	A,N = map(int, f.readline().strip().split())
	motes = map(int ,f.readline().strip().split())
	motes.sort()
	moves = 0

	for i in range(N):
		if A > motes[i]:
			A += motes[i]
		else:
			# check for last
			if i == N-1:
				moves += 1
			else:
				worthit = 0
				done = False
				A2 = A
				while not done:
					x = A2 - 1
					if x == 0:
						moves += 1
						done = True
						continue
					A2 = A2 + x
					worthit += 1
					if worthit < N:
						if A2 > motes[i]:
							moves += worthit
							A = A2 + motes[i]
							done = True
					else:
						moves += 1 #discard element
						done = True
						continue

	if moves > N:
		fo.write('Case #%d: %s\n' % (T+1, N))
	else:
		fo.write('Case #%d: %s\n' % (T+1, moves))

fo.close()
f.close()
