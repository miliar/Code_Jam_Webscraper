def exp_goro(size):
    if size == 1:
        return 0.0
    else:
        return size*1.0

def exp_goro2(size):
    cached = {}
    if size == 1:
        return 0
    sum = 1
    for x in xrange(1,size):
        sum += exp_goro(x)*1.0/x
    # same size perm:
    sum = sum * size * 1.0 / (size - 1)
    return sum

def cycle_sizes(perm):
    perm = [x-1 for x in perm]
    cycle_sizes = [ ]
    cycle_ids = [ -1 ] * len(perm)
    while -1 in cycle_ids:
        curr_id = max(cycle_ids) + 1
        for i in xrange(len(perm)):
            if cycle_ids[i] == -1:
                curr_elem = i
                curr_head = i
                cycle_ids[i] = curr_id
                cycle_sizes.append(1)
                break
        while perm[curr_elem] != curr_head:
            cycle_sizes[curr_id] += 1
            curr_elem = perm[curr_elem]
            cycle_ids[curr_elem] = curr_id
    print cycle_sizes
    return cycle_sizes      

def goro(perm):
    sum = 0
    for cycle in cycle_sizes(perm):
        sum += exp_goro(cycle)
    return sum

def cjwrap(answerer, input_filename):
    fin = file(input_filename, 'r')
    fout = file('output.txt', 'w')
    inputs = int(fin.readline())
    for i in xrange(inputs):
        output = answerer(fin)
        fout.write("Case #%s: %s\n" % (i+1, output))
    fout.close()

def answer(f):
    f.readline()
    perm = f.readline().split(" ")
    perm = [int(x) for x in perm]
    return goro(perm)
    
cjwrap(answer, 'input.txt')