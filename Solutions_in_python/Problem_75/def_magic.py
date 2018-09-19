from collections import deque
T = int(raw_input())
for j in range(1,T+1):
    S = str.split(raw_input())
    pos = 0
    C = int(S[pos])
    #combination=[]
    #oposite=[]
    comb='    '
    opos='    '
    if C!=0 :
        #ltr = S[pos+1]
        #for i in range(0,C):
        #    combination.append(ltr)
        #pos += 1
        comb = S[pos+1]
        pos +=1
    pos += 1
    D = int(S[pos])
    if D!=0:
        #ltr = S[pos+1]
        #for i in range(0,D):
        #    oposite.append(ltr)
        opos = S[pos+1]
        pos += 1
    pos += 1
    N = int(S[pos])
    Data = list(S[pos+1])
    stack = []
    q = deque()
    for i in range (0, len(Data)):
        
        clear=1
        
        if(len(q)>0):
            #Check for complements
            if (str(Data[i])+str(q[len(q)-1])==(comb[0]+comb[1])) or (str(q[len(q)-1])+str(Data[i])==comb[0]+comb[1]):
                try:
                    temp = stack.pop()
                    if (q[len(q)-1])!=temp:
                        stack.append(temp)
                except IndexError:
                    n=1
                q.pop()
                q.append(comb[2])
                clear = 0
                    
        #Check for oposites
        if Data[i]==opos[0] and clear!=0:
            if stack.count(opos[1])>0:
                q.clear()
                stack = []
            else:    
                stack.append(Data[i])
                q.append(Data[i])
            clear = 0
                    
        elif Data[i]==opos[1] and clear!=0:
            if stack.count(opos[0])>0:
                q.clear()
                stack = []
            else:
                stack.append(Data[i])
                q.append(Data[i])
            clear = 0
        #without two conditions only add to queue
        
        if clear!=0:
            q.append(Data[i])
    
    Result = '['
    if(len(q)>0):
        for char in q:
            Result += char+", "
        Result=Result[:-1]
        Result=Result[:-1]
    Result+=']'
    print "Case #"+str(j)+": "+Result
        
    
   