# ------------------------------------------------------------------------------
# globals
# ------------------------------------------------------------------------------
xwon = "X won"
owon = "O won"
draw = "Draw"
notyet = "Game has not completed"

def check_rows(a):
	lines = range(len(a))
	cols = range(len(a[0]))
	line_results = range(len(a))

	for i in lines:
		comp_elt = False
		draw_flag = False

		for j in cols:
			# Set comp_elt
			if j == 0 or comp_elt == False:				
				if a[i][j] == ".":
					line_results[i] = notyet
					break
				else:
					if a[i][j] == "T":
						# skips T comp_elt
						continue 
					else:
						comp_elt = a[i][j]

			# Assuming comp_elt is already set
			else:				
				if a[i][j] == comp_elt or a[i][j] == "T":
					# check winner
					if j == cols[-1]:
						if not draw_flag:							
							return 1, xwon if comp_elt == 'X' else owon
					continue
				else:
					if a[i][j] == ".":
						line_results[i] = notyet
						break;
					else:
						if j == cols[-1]:														
							line_results[i] = draw
						draw_flag = True
						continue
	
	for k in lines:
		if line_results[k] == notyet:
			return 0, notyet
	return 0, draw

def check_cols(a):	
	a2 = [list(tup) for tup in zip(*a)]
	return check_rows(a2)
	
def check_diags(a):
	t = range(len(a))
	diag1 = []
	diag2 = []

	for i in t:
		diag1.append(a[i][i])
		diag2.append(a[i][len(a)-1-i])

	diag = [diag1,diag2]
	return check_rows(diag)
# ------------------------------------------------------------------------------
# solution
# ------------------------------------------------------------------------------

f = open('in')
fo = open('out', 'w')

a = range(4)
for T in range(int(f.readline())):		
	for i in range(4):
		a[i] = list(f.readline().strip())
	f.readline() # skip empty line
	rwho = 0
	cwho = 0
	dwho = 0
	win = 0

	win,rwho = check_rows(a)
	if win:
		print 'Case #%d:' % (T+1), rwho
		fo.write('Case #%d: %s\n' % (T+1, rwho))
		continue
	else:		
		win,cwho = check_cols(a)
		if win:
			print 'Case #%d:' % (T+1), cwho
			fo.write('Case #%d: %s\n' % (T+1, cwho))
			continue
		else:
			win,dwho = check_diags(a)
			if win:
				print 'Case #%d:' % (T+1), dwho
				fo.write('Case #%d: %s\n' % (T+1, dwho))
				continue

	nowinners = [rwho, cwho, dwho]
	try:
		nowinners.index(notyet)
		print 'Case #%d:' % (T+1), notyet
		fo.write('Case #%d: %s\n' % (T+1, notyet))
	except:
		print 'Case #%d: %s' % (T+1, draw)
		fo.write('Case #%d: %s\n' % (T+1, draw))

fo.close()
f.close()
