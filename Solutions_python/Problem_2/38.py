

class case(object):
    
    def __init__(self):
        
        self.T = int(raw_input())
        self.NA, self.NB = map(int,raw_input().split())
        
        self.atob = self.parsetimes(self.NA)
        self.btoa = self.parsetimes(self.NB)
        
        self.a = [(i[0],1) for i in self.atob] + [(i[1]+self.T,0) for i in self.btoa]
        self.a.sort()
        
        self.b = [(i[0],1) for i in self.btoa] + [(i[1]+self.T,0) for i in self.atob]
        self.b.sort()
        
        self.A = 0
        self.B = 0
        
        self.ca = 0
        self.cb = 0
        
        for x,t in self.a:
            if t: # train is leaving
                if not self.ca:
                    self.ca += 1
                    self.A  += 1
                self.ca -= 1
                
            else:
                self.ca += 1
            
        for x,t in self.b:
            if t: # train is leaving
                if not self.cb:
                    self.cb += 1
                    self.B  += 1
                self.cb -= 1
                
            else:
                self.cb += 1
            
    def parsetimes(self, n):
        r = []
        for i in xrange(n):
            dep, ari = raw_input().split()
            
            dep = int(dep[0:2])*60 + int(dep[3:5])
            ari = int(ari[0:2])*60 + int(ari[3:5])
            
            r.append((dep, ari))
        return r
    
    
if __name__ == '__main__':
    
    N = int(raw_input())
    for i in xrange(N):
        c = case()
        
        print 'Case #%d: %d %d' % (i+1, c.A, c.B)
        