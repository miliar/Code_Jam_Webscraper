# -*- coding: utf-8 -*-

import sys

class CodeJamBase(object):
	"""
	base class for all codejam challenges
	"""

	def __init__(self):
		self.inf = None
		self.outf = None
		self.case_num = 0

	def run_tests(self, infilename):
		"""
		run through all tests
		"""
		self.inf = open(infilename, 'r')
		self.outf = open(infilename+"_output.txt", 'w')

		cases = int(self.inf.readline().strip())
		while self.case_num < cases:
			self.case_num += 1
			print "+++ Solving case %s +++" % self.case_num
			self._collect_args()	# store arguments at class level
			res = self._test()
			self._print_out(res)

		self.inf.close()
		self.outf.close()

	def _collect_args(self):
		"""
		collect arguments from the input file
		store them in class arguments
		"""
		raise NotImplementedError()

	def _test(self):
		"""
		run a single test case
		"""
		raise NotImplementedError()

	def _print_out(self, res):
		"""
		print an output line to the output file

		:param res: list of arguments which are split in a list
		"""
		line = " ".join(res)
		self.outf.write("Case #%s: %s\n" % (self.case_num, line))

	def _read_line_as_list(self):
		"""
		read a line from self.inf and return a list of elements
		"""
		return self.inf.readline().strip().split()

	def _read_line_as_string(self):
		return self.inf.readline().strip()

def main():
	"""
	copy this into any actual challenge solcing code
	"""
	sim = CodeJamBase()
	sim.run_tests(sys.argv[1])

if __name__ == "__main__":
	main()