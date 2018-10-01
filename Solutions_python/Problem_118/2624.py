def a(lines):
	class Case:
		def __init__(self, case_lines):
			self.board = []
			for line in case_lines:
				self.board.append(list(line[:-1]))

		def has_blank(self):
			for i in range(len(self.board)):
				for j in range(len(self.board[i])):
					if self.board[i][j] == '.':
						return True
			return False

	def check_list(l):
		mark = l.pop()
		if mark == '.':
			return ''
		if mark == 'T':
			mark = l.pop()
		for ch in l:
			if not ch == mark and not ch == 'T':
				return ''
		return mark

	def process_case(x, case):
		# horizontal
		for i in range(len(case.board)):
			mark = check_list(list(case.board[i]))
			if not mark == '':
				return 'Case #%d: %s won' % (x, mark)

		# vertical
		for j in range(len(case.board[0])):
			l = []
			for i in range(len(case.board)):
				l.append(case.board[i][j])
			mark = check_list(l)
			if not mark == '':
				return 'Case #%d: %s won' % (x, mark)

		# diagonals
		l = []
		for i in range(len(case.board)):
			l.append(case.board[i][i])
		mark = check_list(l)
		if not mark == '':
			return 'Case #%d: %s won' % (x, mark)

		l = []
		for i in range(len(case.board)):
			l.append(case.board[i][3 - i])
		mark = check_list(l)
		if not mark == '':
			return 'Case #%d: %s won' % (x, mark)

		if case.has_blank():
			return 'Case #%d: Game has not completed' % x
		else:
			return 'Case #%d: Draw' % x

	t = int(lines.pop(0))
	out = []

	for i in range(t):
		case_lines = []
		for j in range(4):
			case_lines.append(lines.pop(0))
		lines.pop(0)
		case = Case(case_lines)
		out.append(process_case(i + 1, case))

	return out

def b(lines):
	class Case:
		def __init__(self, lines):
			self.lawn = []
			for line in lines:
				self.lawn.append(map(int, line.split()))

	def is_concave(list):
		pass

	def process_case(x, case):
		pass

	t = int(lines.pop(0))
	out = []

	for i in range(t):
		dims = map(int, lines.pop(0).split())
		case_lines = []
		for j in range(dims[0]):
			case_lines.append(lines.pop(0))
		case = Case(case_lines)
		out.append(process_case(i + 1, case))

	return out

def c(lines):
	import math
	def isPalindrome(num):
		s = str(num)
		for i in range(len(s)):
			if not s[i] == s[-i - 1]:
				return False
		return True

	def process_case(line):
		interval = map(int, line.split())
		count = 0
		for num in range(interval[0], interval[1] + 1):
			if isPalindrome(num):
				root = math.sqrt(num)
 				if root == int(root) and isPalindrome(int(root)):
					count = count + 1
		return count

	t = int(lines.pop(0))
	out = []
	for i, line in enumerate(lines, 1):
		out.append('Case #%d: %d' % (i, process_case(line)))
	return out

def d(lines):
	t = int(lines.pop(0))
	out = []
	return out

