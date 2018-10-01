import numpy as np

def solve(l,k):

    flipInd = np.zeros(len(l),dtype=int);
    activeFlips = 0;    
    v = np.array([x=='+' for x in l]);
    
    for i in range(len(v)):
        if(i>=k and flipInd[i-k]==1):
            activeFlips-=1;
        
        if((v[i]+activeFlips)%2==0):
            if(i>len(v)-k):
                return 'IMPOSSIBLE';
            else:
                flipInd[i] = 1;
                activeFlips+=1;
        
    return str(np.sum(flipInd));
            
    

f = file('/home/jabot/Downloads/A-large.in');
fout = file('/home/jabot/Downloads/A-large.out','w');

lines = f.readlines();
print lines
n = int(lines[0]);
cnt=0;
for l in lines[1:n+1]:
    cnt+=1;
    #print np.array(l.strip().split(' ')[1:],int)
    print '---'
    [l, n] = l.split(' ');
    out = solve(l,int(n))
    
    print out;
    
    fout.write('Case #'+str(cnt)+": "+out+"\n");
    

