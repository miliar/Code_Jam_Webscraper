import re

def binary_2_decimal (k,n):
    #long k, int n
    ## constant = 10000000000000000000000000000000
    #const = 0x80000000
    ##constant = 10000000
    const=2**(n-1)
    output = ""
    ## for each bit
    for i in range(1,(n+1)):
        
        ## if the bit is set, print 1
        if( k & const):
            output = output + "1"
        else:
            output = output + "0"
            
        ## shift the constant using right shift
        const = const >> 1
    
    return output
def test(c,p):
    flag=0
    for i in range(len(c)):
        if c[i]=='1':
            flag=1
            continue
        else:
            flag=0
            break
    if(flag):
        print "Case #"+str(p+1)+": ON"
    else:
        print "Case #"+str(p+1)+": OFF"


#c=binary_2_decimal(0,4)
#print c
#test(c)
infile = open("A-small-attempt2.in","r")
s=infile.readline()
p=re.findall(r'(\d+)', s)
for i in range(int(p[0])):
    s=infile.readline()
    p=re.findall(r'(\d+)', s)
    c=binary_2_decimal(long(p[1]),int(p[0]))
    #print c
    test(c,i)


