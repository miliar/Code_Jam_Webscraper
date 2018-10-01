def parse_inputfile(inf):
    lines=inf.readlines();
    caseno=1;
    totcase=int(lines[0])
    board=[];
    count=0;
    for i in range(1,len(lines)):
        if lines[i]!='\n':
            temp=[]
            for ch in lines[i].strip():
                val=searchval(ch);
                temp.append(val);
            board.append(temp);
            count+=1
            if count==4:
                findstatus(board,caseno);
                count=0;
                caseno+=1;
                board=[]
                
    return

def findstatus(B,caseno):
    rows=[ x for x in B ]
    cols=zip(*B)
    diag1=[r[i] for i, r in enumerate(B)]
    diag2=[r[-i-1] for i, r in enumerate(B)]
    diag=[diag1,diag2]
    flag=0;
    for r in rows:
        sum_r=sum(r)
        flag+=analyse_sum(sum_r,caseno,0)
        if flag!=0:
            break;
        
    for c in cols:
        sum_c=sum(c)
        flag+=analyse_sum(sum_c,caseno,0)
        if flag!=0:
            break;
        
    for d in diag:
        sum_d=sum(d)
        flag+=analyse_sum(sum_d,caseno,0)
        if flag!=0:
            break;

    #SUM of all elements
    sum_a=sum([ sum(x) for x in B ])
    flag+=analyse_sum(0,caseno,sum_a)
    
    if(flag==0):
        if((sum_a==1)|(sum_a==0)):
            print "Case #"+str(caseno)+": Draw";
            flag=1;
    if(flag==0):
        print "Case #"+str(caseno)+": Game has not completed";
    return

def analyse_sum(esum,caseno,asum):
    flg=0;
    if ((esum==4)|(esum==3)):
        print "Case #"+str(caseno)+": X won";
        flg=1;
    elif((esum==-4)|(esum==-3)):
        print "Case #"+str(caseno)+": O won";
        flg=1;
    
    return flg
    
def searchval(ch):
    if ch=='X':
        return 1;
    elif ch=='O':
        return -1;
    elif ch=='T':
        return 0;
    else:
        return 100;
    return



import sys
inf=open(sys.argv[1],'r');
parse_inputfile(inf)
inf.close()


