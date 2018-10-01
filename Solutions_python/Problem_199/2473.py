File=open("A-large.txt",'w')

def flip(s,l_end,size):
    row=s[:l_end]
    row=[c for c in row]
    r_end=l_end+size
    i=l_end
    while i<r_end:
        if s[i]=='+':
            row.append('-')
        elif s[i]=='-':
            row.append('+')
        i=i+1
    for i in range(r_end,len(s)):
        row.append(s[i])
    flipped=''.join(row)
    return flipped

T=int(raw_input())
for t in range(T):
    S,K=[i for i in raw_input().split()]
    K=int(K)
    y=0
    i=0
    while i<len(S)-K+1:
        if S[i]=='+':
            pass
        else:
            S=flip(S,i,K)
            y=y+1
        i=i+1
    if '-' in S:
        print >> File, "Case #%d: IMPOSSIBLE" %(t+1)
    else:
        print >> File, "Case #%d: %d" %(t+1,y)  

File.close()
            
    

