#!/usr/bin/python

qmult = dict((k,dict(zip("1ijk",v.split()))) for k,v in
         [('1', "1 i j k"),
          ('i', "i -1 k -j"),
          ('j', "j -k -1 i"),
          ('k', "k j -i -1")])

def mult(x,y):
    neg = False
    if x[0] == '-':
        neg = not neg
        x = x[1:]
    if y[0] == '-':
        neg = not neg
        y = y[1:]
    res = qmult[x][y]
    if res[0] == '-':
        res = res[1:]
        neg = not neg
    if neg:
        res = '-' + res
    return res

def solve1(f):
    """Solve one instance of the problem"""
    l,x = map(int,f.readline().split())
    line = f.readline().strip()
    group_prod = reduce(mult, line, '1')
    # We can keep multiplying by group_prod to step one group at a
    # time. Further, we can remove groups in sets of 4 without
    # changing the solution, because the product of each group is the
    # same and the product of 4 consecutive groups is therefore 1.

    if x > 12:
        x = (x % 4) + 12
    step = 0
    cur_prod = '1'
    target = ('i','j','k')
    pos = 0
    for i in line * x:
        cur_prod = mult(cur_prod, i)
        #sys.stderr.write(">>> [%d] at: %s, read: %s, prod: %s\n" % (step, pos, i, cur_prod))
        if cur_prod == target[step] and step != 2:
            step += 1
            cur_prod = '1'
        pos += 1
    if cur_prod == 'k' and step == 2:
        # Successful solution!
        return True
    return False

def main(f):
    nprob = int(f.readline())
    for i in range(nprob):
        #sys.stderr.write(">> Case #%d\n"%(i+1))
        sys.stdout.write("Case #%d: %s\n"%(i+1, "YES" if solve1(f) else "NO"))
if __name__ == '__main__':
    import sys
    main(sys.stdin)
        
