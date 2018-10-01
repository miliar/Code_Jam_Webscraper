'''
Created on 12-Apr-2014

@author: tadikond
'''
def magictrick(t,f):
    inp={1:{'array':[],'row':0},2:{'array':[],'row':0}}
    
    inp[1]['row']=int(f.readline())
    for i in range(4):
        row=f.readline()
        rowchar=row.split(" ")
        rowint=[int(j) for j in rowchar]
        inp[1]['array'].append(rowint)
        
    inp[2]['row']=int(f.readline())
    for i in range(4):
        row=f.readline()
        rowchar=row.split(" ")
        rowint=[int(j) for j in rowchar]
        inp[2]['array'].append(rowint)

    set1=set(inp[1]['array'][inp[1]['row']-1])
    set2=set(inp[2]['array'][inp[2]['row']-1])
    
    resultset=list(set1.intersection(set2)) 
    if len(resultset)==0:
        result="Volunteer cheated!"
    elif len(resultset)==1:
        result=str(resultset[0])
    else:
        result="Bad magician!"

    print("Case #"+str(t)+": "+result)

def main(f):
    T=int(f.readline())
    for t in range(T):
        magictrick(t+1,f)

if __name__ == '__main__':
    f=open("A-small-attempt1.in","r")
    
    main(f)