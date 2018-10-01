import collections

def magicka(filename):
    f = open(filename, 'r')
    T = int(f.readline())
    fout = open('B_l2.out', 'w')
##    print "T: %i" % T
    for run in range(T):
        in_str = f.readline().strip('\n')
        result = case(in_str)
        print "Case #%i: %s" % (run+1, result)
        head = 'Case #%i: [' % (run+1)
        fout.write(head)
        fout.write(", ".join(result))
        fout.write(']\n')
        
    f.close()
    fout.close()
    del fout
        


def case(input_str):
    in_q = collections.deque(input_str.split(' '))
##    print len(in_q), in_q
    C = int(in_q.popleft())
    combine = {}
    for comb_num in range(C):
        [c1, c2, cout] = in_q.popleft()
##        print "(%c: %i) + (%c: %d) -> %c" % (c1, ord(c1), c2, ord(c2), cout)
        combine[makekey(c1, c2)] = cout
        combine[makekey(c2, c1)] = cout
##    print 'c: %s' % combine

    D = int(in_q.popleft())
    destroy = {}
    for dest_num in range(D):
        [d1, d2] = in_q.popleft()
        try:
            destroy[d1] += d2
        except KeyError:
            destroy[d1] = d2
        try:
            destroy[d2] += d1
        except KeyError:
            destroy[d2] = d1
##    print 'd: %s' % destroy

    in_q.popleft()
    input_seq = collections.deque(in_q.popleft())
##    print input_seq

    output_seq = collections.deque()
    while len(input_seq) > 0:
        el = input_seq.popleft()
##        print 'in %c' % el,

        if(len(output_seq) == 0):
            output_seq.append(el)
##            print 'app %c' % el,
        else:
            key = makekey(el, output_seq[-1])
            if key in combine:
                el = combine[key]
##                print 'comb %c' % el,
                output_seq.pop()

            output_seq.append(el)
            if el in destroy:
##                print 'chdest %c' % el,
                dest = destroy[el]
                for td in dest:
                    if td in output_seq:
                        output_seq.clear()
##                        print 'dest on %c' % el,
##        print list(output_seq)

    return list(output_seq)

def makekey(c1, c2):
    return ord(c1)*256 + ord(c2)
