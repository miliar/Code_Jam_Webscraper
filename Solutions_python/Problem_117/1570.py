

class ReadHelper(object):
	def __init__(self, file_path, output_path):
		with open(file_path, 'r') as fp:
			with open(output_path, 'w') as op:
				self.num_of_test = int(fp.readline())
				for i in xrange(self.num_of_test):
					n, m = map(int, fp.readline().split(' '))
					content = ''
					for j in xrange(n):
						content += fp.readline()

					matrix = Matrix(n, m, content.strip())
					lawn = Lawn(matrix)
					op.write('Case #{0}: YES\n'.format(i+1)) if lawn.parse() else op.write('Case #{0}: NO\n'.format(i+1))
		fp.close()
		op.close()

class Lawn(object):
	def __init__(self, matrix):
		self.matrix = matrix

	def parse(self):
		while not self.matrix.all_negative():
			scanned = {}
			zero_els = self.matrix.get_zero_els()
			for each in zero_els:
				valid = False
				index_column = each[0]
				index_row = each[1]

				if ((index_column, index_row) in scanned):
					continue
				value = self.matrix.get_el(index_column, index_row)

				# parse row
				row = self.matrix.get_row_contains(index_column, index_row)
				greater = filter(lambda x: x > value, row)
				if len(greater) == 0:
					valid = True
					for i in xrange(len(row)):
						scanned[(i, index_row)] = True

				column = self.matrix.get_column_contains(index_column, index_row)
				greater = filter(lambda x: x > value, column)
				if len(greater) == 0:
					valid = True
					for j in xrange(len(column)):
						scanned[(index_column, j)] = True

				if not valid: return False

			self.matrix.sink()
		return True


class Matrix(object):
	def __init__(self, n, m, content):
		self.n = n
		self.m = m
		self.matrix = []
		for row in content.split('\n'):
			lrow = []
			for el in row.split(' '):
				lrow.append(int(el))
			self.matrix.append(lrow)

	def __repr__(self):
		s = ''
		for row in self.matrix:
			s += ' '.join(map(str, row))
			s += '\n'
		return s

	def get_el(self, column, row):
		if column < 0 or column >= self.m:
			raise ValueError('Row error')

		if row < 0 or row >= self.n:
			raise ValueError('Column error')

		return self.matrix[row][column]

	def get_row_contains(self, column, row):
		if column < 0 or column >= self.m:
			raise ValueError('Row error')

		if row < 0 or row >= self.n:
			raise ValueError('Column error')

		return self.matrix[row]

	def get_column_contains(self, column, row):
		if column < 0 or column >= self.m:
			raise ValueError('Row error')

		if row < 0 or row >= self.n:
			raise ValueError('Column error')

		return [e[column] for e in self.matrix]

	def set_element(self, column, row, value):
		if column < 0 or column >= self.m:
			raise ValueError('Row error')

		if row < 0 or row >= self.n:
			raise ValueError('Column error')

		if type(value) is not int:
			raise TypeError('value not int')

		self.matrix[row][column] = value

	def sink(self):
		for index_row, row in enumerate(self.matrix):
			for index_column, el in enumerate(row):
				self.set_element(index_column, index_row, el - 1)

	def get_zero_els(self):
		els = []
		for index_row, row in enumerate(self.matrix):
			for index_column, el in enumerate(row):
				if el == 0:
					els.append([index_column, index_row, False])
		return els

	def all_negative(self):
		for index_row, row in enumerate(self.matrix):
			for index_column, el in enumerate(row):
				if el >= 0: 
					return False
		return True

if __name__ == '__main__':
	rh = ReadHelper('./B-small-attempt0.in', './result.txt')


