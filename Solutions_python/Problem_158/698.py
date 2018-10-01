def read_data4():
    fin=open('D-small-attempt0.in','r')
    #fin=open('input.txt','r')
    flines=fin.readlines()
    data=[]
    for i in range(1,len(flines)):
        temp=flines[i].split()
        X=int(temp[0])
        R=int(temp[1])
        C=int(temp[2])
        data.append((X,R,C))
    fin.close()
    return data


def solve4((X,R,C)):
    if R*C%X!=0:
        return 'RICHARD'
    if X==1:
        return 'GABRIEL'
    if X==2:
        return 'GABRIEL'
    if X==3:
        if min((R,C))==1:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    if X==4:
        if R*C==4 or R*C==8:
            return 'RICHARD'
        else:
            return 'GABRIEL'
            
def write_results4():
    data=read_data4()
    fout=open('output4.txt','w')
    for i in range(len(data)):
        result=solve4(data[i])
        fout.write('Case #'+str(i+1)+': '+str(result)+'\n')
    fout.close()
        