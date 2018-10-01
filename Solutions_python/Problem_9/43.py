# n, s, engines, queries
# Usage:
# python search.py > out.txt
f = None

def readline():
    return f.readline()

def intline():
    return int(readline())

def DoCase(l):
    k = intline()
    data = map(int, readline().split())
    n = data[0]
    indices = data[1:]

    cards = map(lambda(x): x +1, range(k))
    #print 1
    cards.sort(reverse=True)
    #print 2
    sol = []

    for c in cards:
        #print c, sol
        if not sol:
            sol.append(c)
        elif c == 1:
            sol.insert(0, c)
        else:
            sol.insert(0, c)
            first = c-1
            ls = len(sol)
            first = c - 1 - ((c - 1) / ls * ls)
            #print 'first', first
            part = sol[-first:]
            second = sol[:-first]
            sol = part + second
                

        #print sol
            
    #print 3
    #print v1, v2
    #print 'Case #%d: %d' % (n, num_switches)
    #print sol
    final = []
    for i in indices:
        final.append(sol[i - 1])
    print 'Case #%d: %s' % (l, ' '.join(map(str, final)))
        
def main():
    global f
    f = file('in.txt', 'r')
    line = readline()
    for i in range(int(line)):
        DoCase(i + 1)
    f.close()

if __name__ == '__main__':
    main()
    


