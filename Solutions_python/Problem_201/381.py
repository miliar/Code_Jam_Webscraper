import os
import itertools

class Solver(object):
    def __init__(self):
        pass
    
    def solve(self, inputs):
        N, K = [int(x) for x in inputs[0].split()]
        k = K
        cad = {N : 1}
        cads = [cad]
        while k > 0:
            ncad = {}
            keys = cad.keys()
            keys.sort(reverse=True)
            for key in keys:
                value = cad[key]
                c1 = (key - 1) / 2
                c2 = key - 1 - c1
                k -= value
                if k <= 0:
                    return '%d %d'%(max(c1, c2), min(c1, c2))
                if c1 not in ncad:
                    ncad[c1] = value
                else:
                    ncad[c1] += value
                if c2 not in ncad:
                    ncad[c2] = value
                else:
                    ncad[c2] += value
            cads.append(ncad)
            cad = ncad
            
                

        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            case_line_cnt = 1
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'C-large.in'
    sample_in = '''5
4 2
5 2
6 2
1000 1000
1000 1
    '''
    sample_out = '''
Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499
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