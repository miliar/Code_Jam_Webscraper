inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_yes = "Case #%d: YES"
out_no = "Case #%d: NO"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")

def mul(a,b):
    sign = 1
    if '-' in a:
        sign *= -1
        a = a[1:]
    if '-' in b:
        sign *= -1
        b = b[1:]
    if a=='1':
        return str('-' if sign == -1 else '') + b
    if b=='1':
        return str('-' if sign == -1 else '') + a
    if a==b:
        return str(sign * -1)
    d = {('i','j'): 'k',
     ('j', 'k'): 'i',
     ('k', 'i'): 'j'}
    if (a,b) in d:
        return ('-' if sign == -1 else '') + d[(a,b)]
    else:
        return ('-' if -1*sign == -1 else '') + d[(b,a)]

def case(ncase):
    L, X = parse_line()
    s = rl()
    val = reduce(mul, s)
    #print 'L,X,val', L, X, val
    x = '1'
    for i in xrange(X):
        x = mul(x, val)
    #print 'x', x
    if x != '-1':
        print >>outputfile, out_no % ncase
        return
    s = s*X
    
    cumul = '1'
    for i,c in enumerate(s):
        cumul = mul(cumul, c)
        #print 'i,c,cumul', i,c,cumul
        if cumul == 'i':
            cumul2 = '1'
            for j in xrange(i+1, len(s)):
                cumul2 = mul(cumul2, s[j])
                #print 'cumul2', cumul2
                if cumul2 == 'j':
                    print >>outputfile, out_yes % ncase
                    return
    print >>outputfile, out_no % ncase
    return
        
T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    case(ncase)