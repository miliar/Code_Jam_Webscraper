def read_data():
    fin=open('input.txt','r')
    flines=fin.readlines()
    fin.close()
    cases={}
    T=int(flines[0])
    for t in range(1,T+1):
        cases[t]={}
        cases[t][1]=flines[3*t-3+2].split()
        cases[t][2]=flines[3*t].split()
    cases_num={}
    for k in cases.keys():
        cases_num[k]={}
        for p in cases[k]:
            cases_num[k][p]=[]
            for w in cases[k][p]:
                cases_num[k][p].append(float(w))
    return cases_num

def solve_for_case(case):
    n_points_c=0
    n_points_n=0
    N_weights=case[1]
    N_weights.sort()
    n_weights=N_weights[::-1]
    K_weights=case[2]
    K_weights.sort()
    k_weights=K_weights[::-1]
    
    while len(n_weights)>0:
        
        n=n_weights[0]
        n_weights=n_weights[1:]
        if n>k_weights[0]:
            k_weights=k_weights[:-1]
            n_points_c+=1
        else:
            for k in range(len(k_weights)):
                if n>k_weights[k]:
                    k_weights=k_weights[:k-1]+k_weights[k:]
                    break
            else:
                k_weights=k_weights[:-1]
    n_weights=N_weights[::-1] 
    k_weights=K_weights[::-1]
    while len(n_weights)>0:
        if n_weights[-1]>k_weights[-1]:
            n_weights=n_weights[:-1]
            k_weights=k_weights[:-1]
            n_points_n+=1
        else:
            n_weights=n_weights[:-1]
            k_weights=k_weights[1:]
        
    return n_points_n,n_points_c
    
def run_4():
    cases=read_data()
    fout=open('output.txt','w')
    for k in cases.keys():
        p1,p2=solve_for_case(cases[k])
        fout.write('Case #'+str(k)+': '+str(p1)+' '+str(p2)+'\n')
    fout.close()
        
    
    