#!/usr/bin/env python
import sys

	
class TestCase:
	def __init__(self, data):
		self.C = float(data.split(" ")[0])
		self.F = float(data.split(" ")[1])
		self.X = float(data.split(" ")[2])
		self.total_time = 0.0
		self.total_cookies = 0.0
		self.rate = 2.0
		
	def buyFarm(self):
		self.rate += self.F
		self.total_cookies -= self.C
	
	def isFarmProfitable(self):
		timeA = (self.X - self.total_cookies) / self.rate
		timeB1 = self.C / self.rate
		timeB2 = self.X / (self.rate + self.F)
		timeB = timeB1 + timeB2
		return timeB < timeA
		
	def produceCookies(self, cookies, rate):
		self.total_time += cookies / rate
		self.total_cookies += cookies
		
	def outcome(self):
		while True:
			if self.isFarmProfitable():
				self.produceCookies(self.C - self.total_cookies, self.rate)
				self.buyFarm()
			else:
				self.produceCookies(self.X - self.total_cookies, self.rate)
				break
		return self.total_time




if __name__ == "__main__":
	with open(sys.argv[1]) as df:
		data = df.readlines()

	T = int(data[0])
	
	rf = open("resB.txt", "w")
	for t in range(T):
		case = TestCase(data[t+1].strip())
		outcome = case.outcome()
		rf.write("Case #%s: %s" % ((t+1), outcome))
		if t != T-1:
			rf.write("\n")
	
	rf.close()

