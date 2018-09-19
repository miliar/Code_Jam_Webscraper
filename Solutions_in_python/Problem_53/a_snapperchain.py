class Source:
	
	power=False
	
	def isOn(self):
		return self.power
	
	def toggleOnOff(self):
		self.power = not self.power
	
	def snap(self):
		pass



class Snapper(Source):

	key=False

	def __init__(self,source):
		self.source=source

	def isOn(self):
		return self.source.isOn() and self.key
	
	def toggleOnOff(self):
		self.key = not self.key
	
	def snap(self):
		if self.source.isOn():
			self.toggleOnOff()
		self.source.snap()

class Lamp:
	
	def __init__(self,source):
		self.source=source
	
	def isOn(self):
		return self.source.isOn()
	
	def snap(self):
		self.source.snap()


t = input() #number of tests
for i in range(1,t+1):
	nk = raw_input().split(" ")
	n = int(nk[0]) #number of snappers
	k = int(nk[1]) #number of snaps
	source = Source()
	source.toggleOnOff()
	prev = source
	for j in range(0,n):
		snapper = Snapper(prev)
		prev = snapper
	lamp = Lamp(prev)
	for j in range(0,k):
		lamp.snap()
	print "Case #"+str(i)+": "+ ("ON" if lamp.isOn() else "OFF")


	
