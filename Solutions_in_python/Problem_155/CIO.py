class CIO:

	def __init__(self, src, dest = None):
		if dest == None:
			dest = src.replace(".in", ".out")
		self.fin = open(src, "r")
		self.fout = open(dest, "w")
		self.case = 1
		self.m = self.i()

	def n(self):
		return range(1, self.m+1)

	def sl(self):
		return self.s().split(" ")

	def st(self):
		return tuple(self.sl())

	def s(self):
		return self.fin.readline().replace("\n", "")

	def fl(self):
		return [float(x) for x in self.sl()]

	def ft(self):
		return tuple(self.fl())

	def f(self):
		return self.fl()[0]

	def il(self):
		return [int(x) for x in self.sl()]
	
	def it(self):
		return tuple(self.il())
	
	def i(self):
		return self.il()[0]

	def w(self, data):
		self.fout.write("Case #" + str(self.case) + ": ")
		self.case += 1
		if isinstance(data, list) or isinstance(data, tuple):
			for x in data:
				self.fout.write(str(x) + " ")
		else:
			self.fout.write(str(data))
		self.fout.write("\n")

	def c(self):
		self.fin.close()
		self.fout.close()



