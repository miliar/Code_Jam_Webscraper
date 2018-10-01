def readnums():
    s = raw_input()
    a = s.split()
    return [int(x) for x in a]

def count(b, e, r):
    s = 0
    for i in xrange(r):
        s += b[e][0]
        e = b[e][1]
    return s
    
def main():
    t, = readnums()
    for i in xrange(t):
        r, k, n = readnums()
        a = readnums()
        b = []

        for j in xrange(n):
            s = a[j]
            e = j
            while True:
                e += 1
                
                # wrap arround
                if e == n:
                    e = 0

                # already in
                if e == j:
                    break

                # full
                tt = s + a[e]
                if tt > k:
                    break
                else:
                    s = tt
            
            b.append((s, e))

        """
        ans = 0
        e = 0
        for j in xrange(r):
            print e
            ans += b[e][0]
            e = b[e][1]
        """

        # find cycle
        used = []
        e = 0
        while e not in used:
            used.append(e)
            e = b[e][1]

        # log precycle
        precycle = []
        precycle_sum = 0
        f = 0
        while f != e:
            precycle.append(f)
            precycle_sum += b[f][0]
            f = b[f][1]

        # log cycle
        cycle = []
        cycle_start = e
        cycle_sum = 0
        while e not in cycle:
            cycle.append(e)
            cycle_sum += b[e][0]
            e = b[e][1]
        
        '''
        print k
        print a
        print b
        print 'used:', used
        print 'precycle:', precycle
        print 'cycle:', cycle
        '''

        if r <= len(precycle):
            ans = count(b, 0, r)
        else:
            ans = precycle_sum
            r -= len(precycle)
            
            ans += (r / len(cycle)) * cycle_sum
            r %= len(cycle)
            
            ans += count(b, cycle_start, r)

        print 'Case #%d: %s' % (i + 1, ans)
        
if __name__ == '__main__':
    main()
