from string import split
names=[]
n=[]
consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def inputManip(filename):
    global names, n
    total=0
    lineIndex=1
    inFile=open(filename,"r")
    lines=inFile.readlines()
    inFile.close()
    testCases=int(lines[0][:-1])
    for i in range(1,len(lines)):
        lineList=split(lines[i])
        names+=[(lineList[0])]
        n+=[int(lineList[1])]
    
def substr(string,n_i):
    j=1
    substrings=[]
    while True:
        for i in range(len(string)-j+1):
            substrings+=[string[i:i+j]]
        if j==len(string):
            break
        j+=1
    return n_value(substrings,n_i)

def n_value(substrings,n_i):
    global consonants
    freq=n_v=0
    for string in substrings:
        for letter in string:
            if letter in consonants:
                freq+=1
                if freq==n_i:
                    n_v+=1
                    break

            else:
                freq=0
        freq=0
    return n_v

inputManip("A-small-attempt0.in")
outFile=open("n_value-output.txt","w+")
for i in range(len(names)):
    outFile.write("Case #"+str(i+1)+": "+str(substr(names[i],n[i]))+"\n")
outFile.close()

