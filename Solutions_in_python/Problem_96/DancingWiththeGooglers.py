'''
Created on Apr 14, 2012

@author: Vimuth
'''
inputfile = open('B-large.in','r')
line = int(inputfile.readline());

def checkScore(x,p):
    if x == 0 and p == 0:
        return (True,False);
    if x == 0 :
        return (False,None);
#    y = float(x)/3.0
    if (x>=3*p-2):
        return (True,False);
    elif (x>=3*p-4):
        return (True,True);
    return (False,None);

#print checkScore(12,4);
outputfile = open('output.out','w');

for i in range(0,line):
    text = inputfile.readline();
    contestants = int(text.split(' ')[0])
    suprises = int(text.split(' ')[1])
    minScore = int(text.split(' ')[2])
    count = 0
    for j in range(0,contestants):
        x = checkScore(int(text.split(' ')[3+j]),minScore)
        if (x[0]==True) :
            if x[1]==False:
                count+=1
            elif x[1]==True and suprises>0:
                suprises-=1
                count+=1
             
    l = "Case #"+str(i+1)+": "+str(count)+"\n";
    print l
    outputfile.writelines(l);