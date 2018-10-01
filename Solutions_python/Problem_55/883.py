class NotEnoughSpaceError:
	def __init__(self, msg):
		print "NotEnoughSpaceError:", msg
		
class MaximumRidesPlayedError:
	def __init__(self, msg):
		print "MaximumRidesPlayedError:", msg
		
class NoMoreGroupsException:
	def __init__(self, msg):
		print "NoMoreGroupsException:", msg

class Queue:
	def __init__(self, L):
		self.groups = L
				
	def next(self):
		try:
			return self.groups.pop(0)
		except IndexError:
			raise NoMoreGroupsException("No more groups left in line. Start the ride")
	
	def addToFront(self, g):
		self.groups.insert(0, g)
		
class RollerCoaster:
	def __init__(self, R, k):
		self.maxRides = R
		self.rides = 0
		self.capacity = k
		self.passengers = 0
		self.revenue = 0
		self.groups = []
		
	def addGroup(self, g):
		size = g
		if self.passengers+size > self.capacity:
			raise NotEnoughSpaceError("There is not enough space for a group of size %d" %size)
		else:
			self.groups.append(g)
			self.passengers += size
	
	def ride(self, queue):
		if self.maxRides <= self.rides:
			raise MaximumRidesPlayedError("Maximum number of rides for the day have been played. No more rides today")
		else:
			self.rides += 1
			self.revenue += self.passengers
			self.passengers = 0
			queue.groups += self.groups
			self.groups = []
			
if __name__ == "__main__":
	infilepath = "c:\\users\\administrator\\desktop\\C-small-attempt1.in"
	outfilepath = "c:\\users\\administrator\\desktop\\C-small-attempt1.out"
	
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	num_cases = int(infile.readline())
	lines = infile.readlines()[:num_cases*2]
	
	for i in range(0, len(lines), 2):
		x = (i/2) + 1

		firstLine = lines[i]
		secondLine = lines[i+1]
		
		R, k, N = firstLine.strip().split()
		R, k, N = int(R), int(k), int(N)
		
		secondLine = [int(i) for i in secondLine.strip().split()]
		groups = Queue(secondLine)
		
		rc = RollerCoaster(R, k)
		currGroup = groups.next()
		
		while True:
			try:
				rc.addGroup(currGroup)
			except NotEnoughSpaceError:
				groups.addToFront(currGroup)
				try:
					rc.ride(groups)
				except MaximumRidesPlayedError:
					break
			finally:
				try:
					currGroup = groups.next()
				except NoMoreGroupsException:
					try:
						rc.ride(groups)
						currGroup = groups.next()
					except MaximumRidesPlayedError:
						break
		
		outfile.write("Case #%d: %d\n" %(x, rc.revenue))
		print "Revenue:", rc.revenue
		
	infile.close()
	outfile.close()
	print 'Done!'