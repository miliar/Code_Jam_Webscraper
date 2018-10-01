import math
import pdb

def check_dwar(vs1,vs2):
    score = 0
    k_beg, k_end = 0 , len(vs2)-1
    for n_i in vs1:
        if n_i > vs2[k_beg]:
            score += 1
            k_beg+=1
        else:
            k_end+=1            
    return score

def check_war(vs1,vs2):
    playable = [1]*len(vs2)
    score = 0
    for n_i in vs1:
        for i,k_i in enumerate(vs2):
            if k_i > n_i and playable[i]:
                playable[i] = 0
                break
        else:
            score +=1
    return score  

infile = open('D-large.in','r')
outfile = open('out.txt','w')
T = int(infile.readline())
for t in range(T):
    n = int(infile.readline())
    vs1 = sorted([float(a) for a in infile.readline().split(' ')])
    vs2 = sorted([float(a) for a in infile.readline().split(' ')])
    val1 = check_dwar(vs1,vs2)
    val2 = check_war(vs1,vs2)
##    val2 = check_dwar(vs1,vs2)
    outfile.write('Case #'+str(t+1)+': '+str(val1)+' '+str(val2)+'\n')
    print 'Case #'+str(t+1)+': '+str(val1)+' '+str(val2)
        
infile.close()
outfile.close()
print 'Completed'
                
            
