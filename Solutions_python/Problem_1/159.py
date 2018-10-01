# Google Code Jan 08
from sys import argv
from pprint import pprint
def get_n(f):
    n = int(f.readline())
    i = 0
    result = []
    while i<n:
        i+=1
        result.append(f.readline().strip())
    return n,result
def getind(arr,elem):
    for i,a in enumerate(arr):
        if a==elem: return i
    return len(arr)

if __name__=='__main__':
    f = open(argv[1],'r')
    out = open(argv[1]+'.out','w')
    num_lines = int(f.readline())
    cur_line = 1
    while cur_line<=num_lines:
        e_n,engines_raw = get_n(f)
        engines = dict(zip(engines_raw,range(len(engines_raw))))
        engines_r = dict(zip(range(len(engines_raw)),engines_raw))
        #print 'eng',engines
        n,seq = get_n(f)
        seq = [engines[x] for x in seq]
        switch = []
        #print 'seq',seq
        while seq:
            mx,mx_index = 0,0
            a = [getind(seq,i) for i in range(e_n)]
            mx_index,mx = max(enumerate(a),key=lambda x: x[1])
            switch.append((mx,mx_index))
            seq = seq[mx:]
            #print 'mx',mx,mx_index
            #print 'now',seq
        #print 'seq is',seq
        #print 'solution',len(switch)
        #pprint(switch)
        out.write('Case #%d: %d\n' % (cur_line,max(len(switch)-1,0)))
        print 'Case #%d: %d' % (cur_line,max(len(switch)-1,0))
        cur_line += 1
    out.close()
    f.close()