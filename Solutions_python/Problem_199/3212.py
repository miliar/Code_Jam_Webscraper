import queue as q
f_name='tst_input'
f_name='A-small-attempt1.in'
rows=open(f_name,'r').readlines()
n=int(rows[0])
for tt in range(1,n+1):
    s,k=rows[tt].split()
    end='+'*len(s)
    k=int(k)
    qq=q.Queue()
    qq.put(s)
    done=False
    seen={}
    seen[s]=0
    while(qq.qsize()>0):
        curr=qq.get()
        cnt=seen[curr]
        #print(curr)
        if curr==end:
            print('Case #%d: %d'%(tt,seen[curr]))
            done=True
            break
        for i in range(len(curr)-k+1):
            nxt=curr[:i]
            for j in range(k):
                if curr[i+j]=='+':
                    nxt=nxt+'-'
                else:
                    nxt=nxt+'+'
            nxt=nxt+curr[i+k:]
      #      print(curr[:i],nxt)
            if nxt in seen:
                continue
            seen[nxt]=cnt+1
            qq.put(nxt)
    if not done:
        print('Case #%d: IMPOSSIBLE'%tt)



    


