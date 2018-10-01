test_cases = int(raw_input(''));

def generateTidy(number):
	flag = True;
	numLength = len(number);
	for i in xrange(len(number)-1):
		if (number[i] > number[i+1]):
			flag = False;
	if (not flag):
		return str(int(number[0]) - 1) + '9'*(numLength-1);
	else:
		return number;
for case in xrange(test_cases):
	number = raw_input('');
	for i in range(len(number)-2, -1, -1):
		number = number[:i] + generateTidy(number[i:]);
	
	print 'Case #'+ str(case+1) + ': ' + str(long(number));
