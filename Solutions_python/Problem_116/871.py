import sys, itertools

DEBUG = 0
rl = sys.stdin.readline

def read_game():
	game = []
	for i in xrange(0,4):
		line = rl().strip()
		game += [line]
	rl() # Get rid of empty line
	return game

def check_line(line):
	line_set = set(line)
	if DEBUG:
		print "Check_line: %s -> %s" % (line, line_set)
	if '.' not in line_set:
		if len(line_set) is 1:
			return line_set.pop()
		elif len(line_set) is 2 and 'T' in line_set:
			return (line_set - set('T')).pop()
	return False

def solve(game):
	rows = [check_line(row) for row in game]
	columns = [check_line(column) for column in zip(*game)]
	diagonals_ltor = [check_line([game[i][i] for i in xrange(4)])]
	diagonals_rtol = [check_line([game[i][3-i] for i in xrange(4)])]

	for line in [rows, columns, diagonals_rtol, diagonals_ltor]:
		current = filter(None, line)
		if current:
			return "%s won" % current[0]

	if '.' in itertools.chain(*game):
		return 'Game has not completed'
	else:
		return 'Draw'

def main():
	numcases = int(rl())
	for case in xrange(1, numcases+1):
		game = read_game()
		if DEBUG:
			print "Solving game:\n"
			for line in game:
				print "\t%s" % line
		
		outcome = solve(game)
		print "Case #%d: %s" % (case, outcome)

if __name__ == '__main__':
	main()