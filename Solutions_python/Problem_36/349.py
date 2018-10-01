import sys

pattern_string="welcome to code jam"
pattern_len=len(pattern_string)

def find_possiblities(pattern_i,case_i,case_no,h):
    h+=1
    #print h,pattern_i,case_i,cases_len[case_no],pattern_len,cases_len[case_no]-(pattern_len-pattern_i)+1
    if pattern_i>(pattern_len-1):
        possiblities[case_no]+=1
        return
    #print range(case_i,cases_len[case_no]-(pattern_len-pattern_i)+1)
    for j in range(case_i,cases_len[case_no]-(pattern_len-pattern_i)+1):
        #print h,j,pattern_string[pattern_i],cases[case_no][case_i]
        if pattern_string[pattern_i]==cases[case_no][j]:
            find_possiblities(pattern_i+1,j,case_no,h)
        else:
            continue
    


N=int(sys.stdin.readline())

possiblities=[]
cases=[]
cases_len=[]
for i in range(N):
    inp = sys.stdin.readline()
    cases_len.append(len(inp))
    cases.append(inp)
    possiblities.append(0)
    
for i in range(N):
    find_possiblities(0,0,i,0)
    
for i,pos in  enumerate(possiblities):
    print "Case #%s: %04d" % (i+1,pos)
    
      
