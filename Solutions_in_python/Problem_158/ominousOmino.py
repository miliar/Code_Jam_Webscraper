#encoding: utf-8
import sys
def main():
	inputFile = open(sys.argv[1],'r')
	nTest = int(inputFile.readline())
	for i in range(1,nTest+1):
		line1 = inputFile.readline()
		a = line1.strip().split()
		x = int(a[0])
		r = int(a[1])
		c = int(a[2])
		if r*c < x :
			print "Case #"+ str(i) + ": RICHARD"
		else:
			if (r*c) % x != 0:
				print "Case #"+ str(i)+": RICHARD"
			else:
				if x == 4:
					if r*c == 8:
						print "Case #"+ str(i)+": RICHARD"
					elif r*c == 4:
						print "Case #"+ str(i)+": RICHARD"		
					else:
						print "Case #" + str(i) + ": GABRIEL"
				elif x ==3:
					if r*c == 3:
						print "Case #"+ str(i)+": RICHARD"
					else:	
						print "Case #" + str(i) + ": GABRIEL"
						
				else:
					print "Case #" + str(i) + ": GABRIEL"
				




if __name__ == '__main__':
	main()