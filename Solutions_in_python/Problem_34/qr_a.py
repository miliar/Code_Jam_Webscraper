import sys

def genrate_pattern(p):
    pattern = list()
    
    FLAG = False
    tmp_set = None
    
    p = list(p)
    while p:
        tmp = p.pop(0)
        if tmp == '(':
            FLAG = True
            tmp_set = set()
            continue
        
        if tmp == ')':
            FLAG = False
            pattern.append(tmp_set)
            continue
            
        if FLAG:
            tmp_set.add(tmp)
        else:
            pattern.append(set(tmp))
            
    return pattern
            
def test_word(w, pattern):
    
    w = list(w)
    p = pattern
    for i in range(0,len(p)):
        tmp1 = w[i]
        tmp2 = p[i]
        
        if tmp1 not in tmp2:
            return False
        
    return True
            

if __name__ == '__main__':
    in_file = sys.argv[1]
    rfile = open(in_file)
    L, D, N = rfile.readline().strip().split()
    
    L = int(L); D = int(D); N = int(N)
    tmp = rfile.readlines()
    words = tmp[0:D]
    patterns = tmp[D:]
    
    wfile = open('result_a.txt', 'w')
    n = 0
    for p in patterns:
        n += 1
        p = p.strip()
        pattern = genrate_pattern(p)
        
        count = 0
        for w in words:
            w = w.strip()
            
            if test_word(w, pattern):
                count += 1
                
        wfile.write('Case #'+str(n)+': '+str(count)+'\n')
        
    wfile.close()
        
        
        
        
        
#END