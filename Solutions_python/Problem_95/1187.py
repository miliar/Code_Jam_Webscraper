##abcdefghijklmnopqrstuvwxyz
##ynficwlbkuomxsevdpnrjgthaq
English={'z':'q', 'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j','o':'k', 'm':'l', 'x':'m',  's':'n','e':'o', 'v':'p', 'd':'s', 'p':'r', 'n':'b', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z' , ' ':' '};
def convert(t):
	return English[t];

def ConvertLine(name):
	test=list(name);
	rest=list(map(convert,test));
	return (''.join(rest));
	#print (convert('d'));
	
def readinputfile():
	myfile=open('input.txt');
	outfile=open('output.txt','w');
	TestCases=int(myfile.readline());
	print ("Total number of testcases = " + str(TestCases));
	for TestCase in range(0,TestCases):
		myline = myfile.readline().rstrip().lstrip();
		print ("Case #"+str(TestCase+1)+": "+ConvertLine(myline));
		outfile.write ("Case #"+str(TestCase+1)+": "+ConvertLine(myline)+"\n");
	myfile.close();
	outfile.close();
	
readinputfile();
