TEST = 0;#If 1 prints to console instead of file

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

	def readFormatedLine(self,formater):
		nextline = self.testfile.readline();
		return map(formater, nextline.split())

	def writeresult(self,case,result):
		if TEST:
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

io = casesIO("./D-large.in","./result4.txt");

for i in range(1,io.total+1):
	blocks = io.readDelimiter();
	naomi = io.readFormatedLine(float);
	ken = io.readFormatedLine(float);
	naomi.sort();
	ken.sort();
	kenC = ken[:];
	optScore = 0;
	for j in naomi:
		win = 1;
		for k in ken:
			if k > j:
				ken.remove(k);
				win = 0;
				break;
		if win:
			optScore += 1;
			ken.pop(0)

	cheatScore = 0;
	for j in naomi:
		if kenC[0] < j and kenC[-1] != 1:
			kenC.pop(0);
			cheatScore += 1;
		else:
			kenC.pop();

	io.writeresult(i,"{0} {1}".format(cheatScore,optScore))
	