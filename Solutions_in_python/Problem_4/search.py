# n, s, engines, queries
# Usage:
# python search.py > out.txt
f = None

def DoCase(n):
    f.readline()
    v1 = map(int, f.readline().strip().split())
    v2 = map(int, f.readline().strip().split())

    v1.sort()
    v2.sort(reverse=True)

    #print zip(v1, v2)
    m = lambda(x,y):x * y
    res = sum(map(m, zip(v1, v2)))
    #print v1, v2
    #print 'Case #%d: %d' % (n, num_switches)
    print 'Case #%d: %d' % (n, res)
        
def main():
    global f
    f = file('in.txt', 'r')
    line = f.readline()
    for i in range(int(line)):
        DoCase(i + 1)

if __name__ == '__main__':
    main()
    


