


def PrintRes(Res,num):
	if Res == True:
		fdOut.write("Case #"+str(num+1)+": YES\r\n")
	else:
		fdOut.write("Case #"+str(num+1)+": NO\r\n")

class Dijkstra(object):
		
	def __init__(self,value,sign):
		self.value = value
		self.sign = sign

	def __mul__(self, other):
		if self.value == "1":
			return Dijkstra(other.value, self.sign*other.sign)
		if other.value == "1":
			return Dijkstra(self.value, self.sign*other.sign)
		if self.value == "i":
			if other.value == "i":
				return Dijkstra("1", -self.sign*other.sign)
			if other.value == "j":
				return Dijkstra("k", self.sign*other.sign)
			if other.value == "k":
				return Dijkstra("j", -self.sign*other.sign)
		if self.value == "j":
			if other.value == "i":
				return Dijkstra("k", -self.sign*other.sign)
			if other.value == "j":
				return Dijkstra("1", -self.sign*other.sign)
			if other.value == "k":
				return Dijkstra("i", self.sign*other.sign)
		if self.value == "k":
			if other.value == "i":
				return Dijkstra("j", self.sign*other.sign)
			if other.value == "j":
				return Dijkstra("i", -self.sign*other.sign)
			if other.value == "k":
				return Dijkstra("1", -self.sign*other.sign)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __str__(self):
		if self.sign == 1:
			return self.value
		else:
			return "-"+self.value
		

fdIn = open("/home/aviv/Desktop/Code/CodeJam/2015/dijkstra/C-small-attempt2.in","rb")
fdOut = open("/home/aviv/Desktop/Code/CodeJam/2015/dijkstra/C-small-attempt2.out","w")

Order = ["i","j","k"]

LinesNum=int(fdIn.readline().strip())
for num in xrange(LinesNum):
	rep = int(fdIn.readline().strip().split()[1])
	pattern = fdIn.readline().strip()
	currLetter = Dijkstra("1",1)
	aquired = 0
	for i in xrange(len(pattern)*rep):
		currLetter *= Dijkstra(pattern[i%len(pattern)],1)
		if aquired == 3:
			continue
		if str(currLetter) == Order[aquired]:
			aquired +=1
			currLetter = Dijkstra("1",1)
	if str(currLetter) == "1" and aquired ==3:
		PrintRes(True,num)
	else:
		PrintRes(False,num)

fdIn.close()
fdOut.close()		
		

	
	
	
