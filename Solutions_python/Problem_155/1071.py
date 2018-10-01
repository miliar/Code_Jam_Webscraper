T = int(raw_input())  
for t in xrange(T):
    data = raw_input().split(' ')
    N=int(data[0])
    audience=data[1]
    
    audience_counter=0
    ans=0
    for i in xrange(N+1):
        temp=max(0, i-audience_counter)
        ans+=temp
        audience_counter+=(int(audience[i])+temp)
    
                
              
    print "Case #%d: %s" % (t+1, ans)
  