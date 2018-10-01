import sys
class casesIO:
	def __init__(self,testfilepath,resultfilepath):
		self.testfile = open(testfilepath, 'r');
		self.outfile = open(resultfilepath, 'w');
		self.outlines = 0;
		nextline = self.testfile.readline();
		if not nextline:
			self.total = 0
		else:
			self.total = int(nextline);

	def readDelimiter(self):
		return int(self.testfile.readline());

	def readNumericLine(self):
		nextline = self.testfile.readline();
		return map(int, nextline.split())

	def writeresult(self,case,result,toConsole = 0):

		if toConsole:
			sys.stdout.write("Case #{0}: {1}\n".format(case,result));
		else:
			if self.outlines:
				self.outfile.write("\nCase #{0}: {1}".format(case,result));
			else:
				self.outfile.write("Case #{0}: {1}".format(case,result));
		self.outlines+= 1;

	def __del__(self):
		self.outfile.close()
		self.testfile.close()
TEST = 0;

io = casesIO("./assigment1.txt","./result1.txt");

def getLine():
	line = 0;
	choice = io.readDelimiter();
	if choice >= 1 and choice <=4:
		choice-= 1; #convert so it coresponds to list index
		for j in range(4):
			if j == choice:
				line = io.readNumericLine();
			elif not io.testfile.readline(): #End of file
					break;
	return line;

for i in range(1,io.total+1):
	firstchoice = getLine();
	if not firstchoice: #error end of file reached
		break;
	secondchoice = getLine();
	if not secondchoice: #error end of file reached
		break;
	matching = set(firstchoice) & set(secondchoice)
	mlen = len(matching)
	if mlen == 0:
		io.writeresult(i, "Volunteer cheated!",TEST)
	elif mlen == 1:
		io.writeresult(i, matching.pop(),TEST)
	else:
		io.writeresult(i, "Bad magician!",TEST)