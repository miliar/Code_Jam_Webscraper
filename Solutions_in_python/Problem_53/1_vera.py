if __name__ == "__main__":
    # INICIAL
    T = int(raw_input())
    for line in xrange(1, T+1):
        N, K = raw_input().split()
        N, K = int(N), int(K)
        snappers = []
        
        for i in xrange(1,N+1):
            snappers.append(False)
           
        #logica 
        for estalo in xrange(1, K+1):
            power = 1
            for snapper in snappers:
                if snapper:
                    power = power + 1
                else:
                    break 
            
            power = 1 if power == 0 else power 
            power = power-1 if power > len(snappers) else power
            
            for i in xrange(power):
                snappers[i] = False if snappers[i] else True
    
        #TESTANDO     
        for snapper in snappers:
            if not snapper:
                status = "OFF"
                break
            status = "ON"
        print 'Case #%s: %s' % (line, status)