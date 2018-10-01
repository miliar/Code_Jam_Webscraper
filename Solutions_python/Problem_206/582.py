import os


class Solver(object):
    def __init__(self):
        pass
    
    def solve(self, inputs):
        dist, N = [int(x) for x in inputs[0].split()]
        latest = 0
        for input in inputs[1:]:
            pos, speed = [int(x) for x in input.split()]
            eta = (dist - pos) * 1.0 / speed
            if eta > latest:
                latest = eta
        return '%.6f'%(dist / latest)
        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            ns = [int(x) for x in lines[cur].split()]
            case_line_cnt = 1 + ns[1]
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'A-large.in'
    # iname = 'foo'
    sample_in = '''3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
    '''
    sample_out = '''
Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333
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