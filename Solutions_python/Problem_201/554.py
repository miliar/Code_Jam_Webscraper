def place( spaces, space, no):

	spaces[0][1] -= no
	found = False
	for i in range( 1, 4):
		if spaces[i][0] == space:
			found = True
			spaces[i][1] += no
			break

	if not found:
		first_ind = -1
		for i in range( 1,4):
			if spaces[i][0] == -1:
				first_ind = i
				break
		spaces[first_ind][0] = space
		spaces[first_ind][1] = no

def induce( spaces, no):

	space_remove = no >= spaces[0][1]
	#print "space_remove %s" % space_remove

	remove = no
	if space_remove:
		remove = spaces[0][1]

	space = spaces[0][0]
	#print "space %s" % space
	space -= 1
	rem_small = space // 2
	rem_big = space - rem_small

	if rem_big > 0:
		place( spaces, rem_big, remove)

	if rem_small > 0:
		place( spaces, rem_small, remove)

	#print "before removing:"
	#print spaces
	if space_remove:
		spaces.pop( 0)
		spaces.append( [-1, 0])

	#print "No %s and remove %s" % ( no, remove)
	if no > remove:
		#print spaces
		induce( spaces, no - remove)


def solve( N, K):

	spaces = [0] * 4
	spaces[0] = [N, 1]
	for i in range(1,4):
		spaces[i] = [-1, 0]

	remove = 1
	placed = 0
	while placed + remove < K - 1:
		#print spaces
		#print remove
		induce( spaces, remove)
		placed += remove
		remove *= 2

	remaining = K - 1 - placed
	if remaining > 0:
		#print "remaning %s" % remaining
		#print spaces
		induce( spaces, remaining)

	#print spaces

	#print spaces
	space = spaces[0][0]
	#print space
	space -= 1
	small = space // 2
	big = space - small

	return (big,small)

T = int( raw_input())

no = 1
for i in range(T):
	(N, K) = map(int, raw_input().split())
	(max, min) = solve( N, K)
	print( "Case #%s: %s %s" % (no, max, min))
	no += 1