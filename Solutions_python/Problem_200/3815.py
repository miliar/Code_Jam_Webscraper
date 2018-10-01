
def writeFiles(towrite):
    f.write(towrite+'\n')


def orderValues(intv,i):
#lines=int(input())
#for i in range(lines):
    #intv=input()
    value=list(intv.strip())
    if len(value)==1:
        vall="Case #"+str(i+1)+": "+"".join(value).replace("0","")
        print(vall,sep='')
        writeFiles(vall)
    else:
        for x in range(len(value)-1):
            if(value[x]<=value[x+1]):
                next
            else:
                status=True
                index=x
                while(status):
                    if(index==0):
                        value[index]=str(int(value[index])-1)
                        break
                    if(value[index-1]<=str(int(value[index])-1)):
                        value[index]=str(int(value[index])-1)
                        status=False
                    else:
                        value[index]='9'
                        index-=1
                value[x+1:]=['9']*len(value[x+1:])
                break
        vall="Case #"+str(i+1)+": "+"".join(value).replace("0","")
        print(vall,sep='')
        writeFiles(vall)
                
def openFiles(filename):
    with open(filename) as f:
        i=0
        for line in f:
            if(i>0):
                orderValues(line,i-1)
            i+=1
global f
f = open('B-large.txt', 'w')
openFiles('B-large.in')
f.close()
            
