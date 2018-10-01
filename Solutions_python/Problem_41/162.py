#!/usr/bin/python
import sys

def count(start = 0):
    """docstring for count"""
    x = start
    while 1:
        yield x
        x = x + 1

def get_next(n):
    """docstring for get_next"""
    nlist = [ x for x in "%d" % n if x != '0']
    nlist.sort()
    print nlist
    for i in count(start = n + 1):
        ilist = [ x for x in "%d" % i if x != '0']
        ilist.sort()
        if nlist == ilist:
            print nlist, ilist
            return i

def main():
    """docstring for main"""
    
    f = file(sys.argv[1])
    lines = f.readlines()
    n = int(lines[0].strip())
    f2 = file(sys.argv[1] + ".out", "w")
    for case in range(n):
        test = int(lines[case + 1].strip())
        ans = get_next(test)
        print "Case #%d: %d" % (case + 1, ans)
        f2.write( "Case #%d: %d\n" % (case + 1, ans))
    f2.close()
        
if __name__ == '__main__':
    main()
