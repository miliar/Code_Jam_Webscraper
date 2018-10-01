import sys

def logger(f) :
    def wrapper(*args) :
        printerr('call '+ f.__name__+':', *args)
        ans = f(*args)
        printerr('ret  '+ f.__name__+':', ans)
        return ans
    return wrapper

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    
    return "nothing"

def readline(fun) : 
    return [fun(_) for _ in input().split()]
def once():
    '''to cope once'''
    n, v, x = readline(float)
    n = int(n)
    a = [readline(float) for _ in range(n)]
    a = [(r/v,c-x) for [r,c] in a]
    def check() :
        if all([c < 0 for r,c in a]) or all([c > 0 for r,c in a]) :
            return None
        if any([c == 0 for r,c in a]) :
            return 1 / sum([r for r,c in a if c == 0])
        r1,x1 = a[0]
        r2,x2 = a[1]
        return max(x1/(x1-x2)/r2, x2/(x2-x1)/r1)
    ans = check()
    return ans if ans != None else 'IMPOSSIBLE'
                

def printerr(*v):
    print(*v, file=sys.stderr)

def main():
    TT = int(input())
    for tt in range(1,TT+1):
        printerr("coping Case %d.."%(tt))
        ans = once()
        print("Case #%d: %s"%(tt, (ans)))

if __name__ == '__main__' :
    msg = prework(sys.argv)
    print("prework down with", msg, file=sys.stderr)
    main()
