import sys

class Snapper:
	def __init__(self, parent):
		self.parent = parent
		self.on = False
		self.powered = False

	def flowing(self):
		if self.on and (self.parent==None or self.parent.flowing()) :
			return True
		else:
			return False

	def toggle(self):
		self.on = self.on ^ True

if __name__ == "__main__":

	input_length = int(sys.stdin.readline())

	for i in range(input_length):
		n, k = sys.stdin.readline().split()
		n = int(n)
		k = int(k)
		snapper_list = []
		last_snapper = None
		for j in range(n):
			snapper_list.append(Snapper(last_snapper))		
			last_snapper = snapper_list[-1]
		for j in range(k):
			to_toggle = 0
			for s in snapper_list:
				if s.parent == None or s.parent.flowing():
					to_toggle += 1
				else:
					break

			for x in range(to_toggle):
				snapper_list[x].toggle()


		if snapper_list[-1].flowing():
			result = "ON"
		else:
			result = "OFF"
		print "Case #" + str(i+1) + ": " + result


	
