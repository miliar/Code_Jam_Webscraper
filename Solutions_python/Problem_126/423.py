import string

consts = set(string.letters[:26]) - set('aeiou')

def subsets(s, n):
    for end in range(len(s), n-1, -1):
        for start in range(0, end-n+1):
            yield s[start:end]

def solve(name, n):
    global consts
    num = 0
    for subset in subsets(name, n):
        #print subset, 
        conseq = 0
        for char in subset:
            if char in consts:
                #print '.',
                conseq += 1
            else:
                #print 'E',
                conseq = 0
            if conseq == n:
                num += 1
                #print 'Y'
                break
        else:
            pass
            #print 'N'
    return num



T = int(raw_input())
for i in range(T):
    name, n = raw_input().split(' ')
    n = int(n)
    print 'Case #{0}: {1}'.format(i+1, solve(name, n))

