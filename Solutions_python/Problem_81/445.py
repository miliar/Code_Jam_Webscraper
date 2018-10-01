def findwp(sch):
    w = 0
    l = 0
    for c in sch:
        if c == '1':
            w = w + 1
        elif c == '0':
            l = l + 1
    
    return float(float(w)/float(l+w))

def main():
    #fi = open('A-small-attempt0.in')
    fi = open('A-large.in')
    #fi = open('probelm-a.in')
    fo = open('A-large.out', 'w')
    t = int(fi.readline())
    
    for k in range(t):
        terms = int(fi.readline())
        sch = []
        wp = []
        owp = []
        oowp = []
        w = 0
        l = 0
        for i in range(terms):
            sch.append(fi.readline().rstrip())
        
        for i in range(terms):
            w = 0
            l = 0       
            for c in sch[i]:
                if c == '1':
                    w = w + 1
                elif c == '0':
                    l = l + 1
            
            wp.append(float(float(w)/float(l+w)))
 
        for i in range(terms):
            w = 0
            l = 0       
            _owp = 0.0
            j = 0
            for c in sch[i]:
                if c == '1':
                    w = w + 1
                elif c == '0':
                    l = l + 1
                    
                if c != '.':
                    _sch = list(sch[j])
                    _sch[i]='.'
                    _owp = _owp + findwp(''.join(_sch))
                    #print _owp, c
                    
                j = j + 1
                
            #print _owp, float(w+l)
            owp.append(float(float(_owp)/float(w+l)))
        #print "-"    
        for i in range(terms):
            w = 0
            l = 0       
            _oowp = 0.0
            j = 0
            for c in sch[i]:
                if c == '1':
                    w = w + 1
                elif c == '0':
                    l = l + 1
                    
                if c != '.':
                    _oowp = _oowp + owp[j]
                    #print _oowp, owp[j], c, j
                    
                j = j + 1
            
            #print _oowp, float(w+l)        
            oowp.append(float(float(_oowp)/(w+l)))
        
        #print wp
        #print owp
        #print oowp
        
        #fo.write("Case #%d: %s\n" % (i+1, o))
        fo.write("Case #%d:\n" % (k+1))
        print "Case #%d:" % (k+1)
        for j in range(terms):
            fo.write("%f\n" % float( float(0.25*wp[j]) + float(0.5*owp[j]) + float(0.25*oowp[j]) )   )
            print "%f" % float( float(0.25*wp[j]) + float(0.5*owp[j]) + float(0.25*oowp[j]) )        

if __name__ == "__main__":
    main()