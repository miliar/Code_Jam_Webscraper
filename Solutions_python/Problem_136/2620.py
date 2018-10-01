class Cookie:
	def __init__(self,c,f,x):
		self.c = c
		self.f = f
		self.x = x
		self.cookie = 0.0
		self.building = 0.0
		self.time = 0.0

	def cps(self,building=0):
		if building == 0:
			building = self.building
		return self.f*building + 2

	def testbuy(self):
		need = self.c - self.cookie
		possible = self.cps()
		time = need/possible
		return 1.0*time

	def estimate(self):
		final = self.x - self.cookie
		path_one = self.cps()
		path_two = self.cps(self.building + 1)
		time1 = final/path_one
		time2 = self.testbuy() + final/path_two
		
		return time1>time2

	def buy(self):
		time = self.testbuy()
		self.building = self.building + 1
		self.time = self.time + time
		return time

	def wait(self):
		need = self.x - self.cookie
		possible = self.cps()
		time = need/possible
		self.cookie = self.cookie + need
		self.time = self.time + time
		return time

	def finalize(self):
		needibuy = self.estimate()
		if needibuy:
			self.buy()
		else:
			self.wait()
			raise IndexError

	def run(self):
		try:
			while True:
				self.finalize()
		except:
			pass
		return self.time


t = int(raw_input())
for i in range(t):
	c,f,x, = map(float,raw_input().split())
	temp = Cookie(c,f,x)
	time = temp.run()
	print "Case #%d: %.7f"%(i+1,time)