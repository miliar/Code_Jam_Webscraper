from collections import defaultdict;
inputData = [];
infile = open("A-small.in","r");
line = infile.readline();
TestCases = int(line);
line = infile.readline();
testCase = 0;
while line!="":
    inputData.append(line);
    line = infile.readline();
    testCase+=1;
infile.close();
alphabetMap = {
'a':'y',
'b':'n',
'c':'f',
'd':'i',
'e':'c',
'f':'w',
'g':'l',
'h':'b',
'i':'k',
'j':'u',
'k':'o',
'l':'m',
'm':'x',
'n':'s',
'o':'e',
'p':'v',
'q':'z',
'r':'p',
's':'d',
't':'r',
'u':'j',
'v':'g',
'w':'t',
'x':'h',
'y':'a',
'z':'q',
' ':' '
}
reverseMap = {}
for alpha in alphabetMap:
    value = alphabetMap[alpha];
    reverseMap[value] = alpha;
for i in range(TestCases):
    print "Case #%d: "%(i+1),
    inLine = inputData[i].replace('\n','');
    text = "";
    for char in inLine:
        text+=(reverseMap[char]);
    print text;
    
