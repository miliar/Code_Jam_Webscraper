outfile=open('outfileC_Dj','w')

fil=open("C-small-attempt0.in")
cases=int(fil.readline())
out=""

MULTI_STR=[['x','1','i','j','k'],
           ['1','1','i','j','k'],
           ['i','i','-1','k','-j'],
           ['j','j','-k','-1','i'],
           ['k','k','j','-i','-1']]

def multpl_quart(quart1, quart2, multp_str):
    ind_q1= [ind for ind in xrange(5) if MULTI_STR[ind][0]==quart1][0]
    ind_q2= [ind for ind in xrange(5) if MULTI_STR[0][ind]==quart2][0]
    return MULTI_STR[ind_q1][ind_q2]

for case in xrange(cases):
        line=fil.readline().split()
        NBR=int(line[1])
        line=fil.readline().split()
        S=line[0]*NBR
        DJKS="ijk"; ind_djks=0; res=""; Neg=0; i=0
        
        while i<len(S)-1:
            if S[i]=="-":
                Neg+=1
                S=S[1:]         
            else:
                if ind_djks<2:
                    if S[i]==DJKS[ind_djks] :
                        ind_djks+=1
                        res+=S[i]
                        S=S[1:]         
                    else:
                        mult=multpl_quart(S[i],S[i+1],MULTI_STR)
                        if mult==DJKS[ind_djks]:
                            res+=mult
                            ind_djks+=1
                            S=S[2:]
                        else: S=mult+S[2:] 
                else : S=multpl_quart(S[i],S[i+1],MULTI_STR)+S[2:]
                
        if res+S==DJKS and Neg%2==0:
            final_res="YES"
        else:
            final_res="NO"
        out+=("Case #%d: %s\n")%( case+1, final_res)
    
print out
outfile.write(out)
outfile.close()
