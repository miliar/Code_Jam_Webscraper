import time
#vars
fin = open("b0.in","r")
fout = open("b0.out","w")
l=0
d=0
n=0
words = []
count = 0
code = ""
cidx = 0 #current index
#--------------------------------------

def getSeq():
    global code,cidx
    if code[cidx] != "(":
        t = code[cidx]
        cidx +=1
        return t
    else:
        t = code[cidx+1:code.index(")",cidx)]
        cidx = code.index(")",cidx)+1
        return t
    
def calc():
    global words,code,cidx,count
    seq = ""
    for word in words:
        cidx = 0
        found = True
        for i in range(0,len(word)):
            seq = getSeq()
            if (seq.find(word[i]) < 0):
                found = False
                break
        if found == True:
            count+=1
            
        
            

#--------------------------------------
#read the first line to get l , d and n
line= fin.readline()
l = int(line.split()[0])
d = int(line.split()[1])
n = int(line.split()[2])
for i in range(0,d):
    words.append(fin.readline()[:-1])


for i in range(0,n):
    #print "case " + str(i)
    code = fin.readline()[:-1]
    count = 0
    #start = time.time()
    #print code
    #print getSeq(),getSeq(),getSeq()
    calc()
    #end = time.time()
    #print count
    fout.write("Case #" + str(i+1) + ": " + str(count) + "\n")
    #print "time",end-start

fin.close()
fout.close()
    
