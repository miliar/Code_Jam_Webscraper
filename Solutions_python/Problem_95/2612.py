import sys;

mapping = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x',' ':' ', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'};

i=0;
c=1;
word="";
multiline = [];
newmultiline = [];
var1=raw_input( "Enter the No.of Lines\n");
if int(var1)<1 or int(var1)>30:
	print ("Not in range !");
	sys.exit();
print("Enter "+var1+" Lines\n");
while i< int(var1):
	var=raw_input("");
	multiline.append(var);
	i+=1;

for x in multiline:
	word="";
	for let in x:
		word+=mapping[let];	
	newmultiline.append(word);


for p in newmultiline:
	print "Case #"+str(c)+": "+p;
	c+=1;

