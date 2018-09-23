import os

class Rect(object):
    def __init__(self, char, r, c):
        self.char = char
        self.left = c
        self.right = c
        self.top = r
        self.bottom = r
    
    def include(self, r, c, cad):
        if c < self.left:
            self.left = c
        if c > self.right:
            self.right = c
        if r < self.top:
            self.top = r
        if r > self.bottom:
            self.bottom = r
            
    def fill(self, cad):
        for r in range(self.top, self.bottom+1):
            for c in range(self.left, self.right+1):
                cad[r][c] = self.char
        
    def exLeft(self, cad):
        if self.left == 0:
            return False
            
        c = self.left - 1
        for r in range(self.top, self.bottom+1):
            if cad[r][c] != '?' and cad[r][c] != self.char:
                return False
                
        for r in range(self.top, self.bottom+1):
            cad[r][c] = self.char
        self.left = c    
        return True
        
    def exRight(self, cad):
        if self.right == len(cad[0])-1:
            return False
            
        c = self.right + 1
        for r in range(self.top, self.bottom+1):
            if cad[r][c] != '?' and cad[r][c] != self.char:
                return False
                
        for r in range(self.top, self.bottom+1):
            cad[r][c] = self.char
        self.right = c    
        return True
            
    def exBottom(self, cad):
        if self.bottom == len(cad)-1:
            return False
            
        r = self.bottom + 1
        for c in range(self.left, self.right+1):
            if cad[r][c] != '?' and cad[r][c] != self.char:
                return False
                
        for c in range(self.left, self.right+1):
            cad[r][c] = self.char
        self.bottom = r    
        return True
        
    def exTop(self, cad):
        if self.top == 0:
            return False
            
        r = self.top - 1
        for c in range(self.left, self.right+1):
            if cad[r][c] != '?' and cad[r][c] != self.char:
                return False
                
        for c in range(self.left, self.right+1):
            cad[r][c] = self.char
        self.top = r    
        return True

class Solver(object):
    def __init__(self):
        pass
    
    def ff(self, row):
        for i in range(len(row)):
            if row[i] != '?':
                return i, row[i]
        return -1, '?'
    
    def solve(self, inputs):
        R, C = [int(x) for x in inputs[0].split()]
        
        
        cad = [list(x) for x in inputs[1:]]

        dd = {}
        for r in range(R):
            for c in range(C):
                char = cad[r][c]
                if char != '?':
                    if char not in dd:
                        dd[char] = Rect(char, r, c)
                    else:
                        dd[char].include(r, c)
        for v in dd.values():
            v.fill(cad)
        
        for v in dd.values():
            while v.exLeft(cad): pass
            while v.exTop(cad): pass
            while v.exRight(cad): pass
            while v.exBottom(cad): pass
        
        return '\n' + '\n'.join([''.join(x) for x in cad])
            
        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            r, c = [int(x) for x in lines[cur].split()]
            case_line_cnt = 1 + r
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'A-small-attempt0.in'
    # iname = 'foo'
    sample_in = '''3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
    '''
    sample_out = '''
Case #1:
GGJ
CCJ
CCJ
Case #2:
CODE
COAE
JJAM
Case #3:
CA
KE
    '''
    if os.path.exists(iname):
        with open(iname) as f:
            inputs = f.readlines()
    else:
        inputs = [x.strip() for x in sample_in.split('\n') if x.strip()]
    solver = Solver()
    outputs = solver.feed(inputs)
    fail_flag = False
    if os.path.exists(iname):
        with open(iname+'.out', 'w') as f:
            for i, v in enumerate(outputs):
                print >> f, 'Case #%d: %s'%(i+1, str(v))
    else:
        ans = set([x.strip() for x in sample_out.split('\n') if x.strip()])
        for i, v in enumerate(outputs):
            t = 'Case #%d: %s'%(i+1, str(v))
            if t not in ans:
                print '!!! Wrong:', t
                fail_flag = True
    print '===================================================='
    for i, v in enumerate(outputs):
        print 'Case #%d: %s'%(i+1, str(v))
    print '===================================================='
    print 'done' if not fail_flag else 'fail'
    pass