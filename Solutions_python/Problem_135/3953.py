ar=[]
def main(filename,outfile):
    output=open(outfile,'w')
    with open(filename,mode='r') as f:
        for line in f.readlines():
            ar.append(line)
    tt=int(ar.pop(0))
    i=0
    while i<tt:
        s=magic(i*10)
        output.write("Case"+' '+"#%d:"%(i+1)+' '+s+"\n");
        i=i+1
    output.close()
    print "Done"
        



def magic(k):
    a=int(ar[k])
    b=int(ar[k+5])
    rset=set(ar[a+k].split()).intersection(set(ar[b+k+5].split()))
    if len(rset)==1:
        return rset.pop()
    elif len(rset)>1:
        return "Bad magician!"
    elif len(rset)==0:
       return "Volunteer cheated!"
        
        

    
            

            
        
