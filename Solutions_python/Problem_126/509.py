VOWELS = ['a','e','i','o','u']

def memo(fn):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            r = cache[args] = fn(*args)
            return r
        except TypeError:
            print 'hey'
            return fn(*args)
    return _f

#@memo
def check_consonants(s,n):
    N = len(s)
    if N < n:
        return False
    for i in xrange(N-n+1):
        c = 0
        for j in xrange(i,i+n):
            if s[j] not in VOWELS:
                c+=1
            else:
                break
        if c == n:
            return True
    return False
            
def solve(*args):
    name,n = args[0].split()
    n = int(n)
    N = len(name)
    retVal = 0
    for i in xrange(N):
        for j in xrange(i+1,N+1):
            #print name[i:j]
            if check_consonants(name[i:j],n):
                retVal += 1
    return retVal

cases = int(raw_input())
for case in xrange(cases):
    print str.format('Case #{0}: {1}',case+1,solve(raw_input()))

