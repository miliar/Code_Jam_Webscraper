# code jam B

def solve(problemid,data):
    data=[map(int,x.split()) for x in data]
    H,W=len(data),len(data[0])
    flows={}
    cells=[(r,c) for r in range(H) for c in range(W)]
    for (r,c) in cells:
        height=data[r][c]
        tocells=[(r+dr,c+dc) for (dr,dc) in [(0,-1),(1,0),(0,1),(-1,0)]
                 if r+dr>=0 and c+dc>=0 and r+dr<H and c+dc<W]
        stuff=[(data[rr][cc],(rr,cc)) for (rr,cc) in tocells]
        if stuff:
            possflowto=min(stuff)
        else:
            possflowto=[]
        if possflowto and possflowto[0]<height:
            flowto=possflowto[1]
            flows[(r,c)]=flows.get((r,c),[])+[flowto]
            flows[flowto]=flows.get(flowto,[])+[(r,c)]
            
    print problemid
            
    ans=[['_' for i in range(W)] for j in range(H)]
    code=0
    while True:
        unmarked=[(r,c) for (r,c) in cells if ans[r][c]=='_']
        if unmarked:                
            # mark the first unmarked one
            (rr,cc)=min(unmarked)
            code+=1
            ans[rr][cc]=chr(96+code)    
            # fill in basins until filling no more
            # ie look for unmarked ones which flow to a marked one
            # if there are any then mark them
            # if not, then move on
            numfilled=1
            while numfilled!=0:
                numfilled=0
                for (r,c) in cells:
                    if ans[r][c]=='_':
                        basin=[ans[rr][cc] for (rr,cc) in flows.get((r,c),[]) if ans[rr][cc]!='_']
                        if basin:
                            ans[r][c]=basin[0]
                            numfilled+=1
        else:
            break
    return 'Case #'+str(problemid)+':\n'+'\n'.join([' '.join(x) for x in ans])
            

# load data
datain="""
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8
"""
#or
datain=open("B-large.in").read()
dataout=open("B-large.out","w")

data=[x for x in datain.split('\n') if x]
N=int(data[0])
row=1
for i in range(N):
    H,W=map(int,data[row].split())
    text=solve(i+1,data[row+1:row+H+1])
    dataout.write(text+'\n')
    row+=H+1




dataout.close()

