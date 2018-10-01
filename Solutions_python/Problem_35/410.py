import numpy
import pdb

def solve_case(alt_array):
    s = alt_array.shape
    if len(s) < 2:
        s = (s[0], 1)
    label_queue = 'abcdefghijklmnopqrstuvwxyz'
    
    def find_flow(i, j):
        m = alt_array[i,j]
        d = -1
        if i > 0 and m > alt_array[i-1,j]:
            m = alt_array[i-1,j]
            d = 0
        if j > 0 and m > alt_array[i,j-1]:
            m = alt_array[i,j-1]
            d = 1
        if j < s[1] - 1 and m > alt_array[i,j+1]:
            m = alt_array[i,j+1]
            d = 2
        if i < s[0] - 1 and m > alt_array[i+1,j]:
            m = alt_array[i+1,j]
            d = 3
        return d
    
    # -1 sink
    # 0 north
    # 1 west
    # 2 east
    # 3 south
    flows = numpy.zeros(s)
    for i in xrange(0, s[0]):
        for j in xrange(0, s[1]):
            flows[i,j] = find_flow(i, j)
    
    label_stack = range(1, 27)
    label_stack.reverse()
    labels = numpy.zeros(s, dtype='int')
    
    def find_label(i, j):
        """Label, 0 if unlabeled"""
        #pdb.set_trace()
        if labels[i,j] != 0:
            return labels[i,j]
        flow = flows[i,j]
        if flow == -1:
            labels[i, j] = label_stack.pop()
        elif flow == 0:
            labels[i,j] = find_label(i-1, j)
        elif flow == 1:
            labels[i,j] = find_label(i, j-1)
        elif flow == 2:
            labels[i,j] = find_label(i, j+1)
        elif flow == 3:
            labels[i,j] = find_label(i+1, j)
        else:
            raise Exception("uh oh")
        return labels[i, j]
    
    #pdb.set_trace()
    
    for i in xrange(0, s[0]):
        for j in xrange(0, s[1]):
            find_label(i, j)
    
    @numpy.vectorize
    def to_char(n):
        return label_queue[n-1]
    
    return numpy.char.array(to_char(labels))

if __name__ == '__main__':
    import sys
    
    lines = [l.strip() for l in open(sys.argv[1])][1:]
    
    cases = []
    while lines:
        h, w = lines.pop(0).split()
        h, w = int(h), int(w)
        
        case, lines = lines[:h], lines[h:]
        case = [[int(x) for x in l.split()] for l in case]
        cases.append(numpy.array(case, dtype="int"))
    
    i = 0
    for case in cases:
        i += 1
        solution = solve_case(case)
        print 'Case #%i:' % i
        for line in solution:
            print ' '.join([x for x in line])
        
