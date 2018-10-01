import copy

N=[]
fname="B-large.in"
f=open(fname)
T=f.readline()
for aux in f:
    N.append(aux.split()[0])
    
def convert(a):
    l=[]
    for aux in a:
        l.append(int(aux))
    return l

def unconvert(a):
    l=''

    for aux in a:
        l=l+str(aux)
    return str(int(l))
        
g = open("output.out", "w")
T=1   

for num in N:
    test=convert(num)
    test.reverse()
    tidy=copy.copy(test)
    
    
    for i in xrange(1,len(tidy)):  

        if tidy[i-1] < tidy[i]:
            #print tidy
            tidy[i]=tidy[i]-1
            tidy[0:(i)]=[9]*(i)
               
    test.reverse()
    tidy.reverse()
    print unconvert(test), unconvert(tidy)
    g.write('Case #'+str(T)+': ' + unconvert(tidy) +'\n')
    T+=1

        
    