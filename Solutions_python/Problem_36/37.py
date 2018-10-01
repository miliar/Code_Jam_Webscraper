import string

inputFile = "C-large.in";
outputFile = "C-large.out";

s = "welcome to code jam";
indicators = {};

def main():	
	fdin = open(inputFile);
	fdout = open(outputFile, 'wb');
	
	casecountString = fdin.readline();
	caseCount = int(casecountString);
	for c in s:
		if not indicators.has_key(c):
			indicators[c]=[];
	for k in range(caseCount):
		line = fdin.readline();	
		result = processCase(line);
		resultLine = "Case #" + str(k+1) + ": %04d"%result + "\n";
		fdout.write(resultLine);

def processCase(line):
	for key in indicators.keys():
		indicators[key]=[];
		rline = line;
		while True:
			pos=rline.rfind(key);
			if pos == -1:
				break;
			indicators[key].append(pos);
			rline=rline[:pos];
		if indicators[key] == []:
			return 0;
	rstr= s[::-1];
	table=[];
	line1 = [];
	counter =1;
	for index in indicators['m']:
		line1.append([index, counter]);
		counter = counter + 1;
	table.append(line1);
	for i in range(1, len(rstr)):
		table.append([]);
		c = rstr[i];
		count = 0;
		for index in indicators[c]:
			for j in range(len(table[i-1])):
				if table[i-1][j][0] <= index:
					j = j-1;
					break;
			if j>=0:
				count = count + table[i-1][j][1];
			if count > 10000:
				count = count%10000;
			table[i].append([index, count]);
	lastline=table[18];
	return lastline[len(lastline)-1][1];
		
			
	
				
				
				
	

if __name__ == "__main__":
    main()
