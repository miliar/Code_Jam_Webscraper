def go():
    f=open('e:\\downloads\\1.txt')
    for x in range(int(f.readline())):
        engines=[]
        queries=[]
        switches=0
        zero=False
        for y in range(int(f.readline())):
            engines.append(f.readline())
        for y in range(int(f.readline())):
            queries.append(f.readline())


        for a in engines:
            if a not in queries:
                break #zero
        
        last=set(engines)
        for b in queries:
            
            
            if b in last:
                last.remove(b)
            if len(last)==0:
                switches+=1
                last=set(engines)
                last.remove(b)
                
            
                    
        print 'Case #%d: %d'%(x+1,switches)
                    
                
                
go()
