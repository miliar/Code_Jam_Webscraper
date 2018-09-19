inputData = [];
infile = open("C-small-attempt3.in","r");
line = infile.readline();
TestCases = int(line);
line = infile.readline();
testCase = 0;
while line!="":
    fields = line.split();
    inputData.append((int(fields[0]),int(fields[1])));
    line = infile.readline();
    testCase+=1;
infile.close();

def getCount(start,end):
    count = 0;
    newStrings = []
    for i in range(start,end):
        for index in range(1,len(str(i))):
            string = str(i);
            newString = string[index:]+string[0:index];
            newStringIntVal = int(newString);
            if newStringIntVal <= end and newStringIntVal >= start and(newStringIntVal < i):
                newStrings.append((i,newStringIntVal));
                count+=1;
    return len(set(newStrings));


for i in range(TestCases):
    print "Case #%d: %d"%(i+1,getCount(inputData[i][0],inputData[i][1]+1));
    
