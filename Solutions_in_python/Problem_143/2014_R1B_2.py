def solve_small(a,b,k):
    count=0
    for i in range(a):
        for j in range(b):
            if i&j<k:
                count+=1
    return str(count)
def read_data():
    cases={}
    fin=open('input.txt','r')
    flines=fin.readlines()
    fin.close()
    n=0
    for i in range(1,len(flines)):
        n+=1
        line=flines[i].split()
        cases[n]=[int(line[0]),int(line[1]),int(line[2])]
    return cases

def solve_1B():
    fout=open('output.txt','w')
    cases=read_data()
    for i in range(len(cases)):
        a=cases[i+1][0]
        b=cases[i+1][1]
        k=cases[i+1][2]
        result=solve_small(a,b,k)
        fout.write('Case #'+str(i+1)+': '+result+'\n')
    fout.close()
        
    
    