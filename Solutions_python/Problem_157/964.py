## Dijkstra
num_of_case = int(raw_input())

rule1 = {'11':( 1, '1'),
        '1i':( 1, 'i'),
        '1j':( 1, 'j'),
        '1k':( 1, 'k'),
        'i1':( 1, 'i'),
        'ii':(-1, '1'),
        'ij':( 1, 'k'),
        'ik':(-1, 'j'),
        'j1':( 1, 'j'),
        'ji':(-1, 'k'),
        'jj':(-1, '1'),
        'jk':( 1, 'i'),
        'k1':( 1, 'k'),
        'ki':( 1, 'j'),
        'kj':(-1, 'i'),
        'kk':(-1, '1')
        }
        
rule2 = {'11':( 1, '1'),
         'i1':(-1, 'i'),
         'j1':(-1, 'j'),
         'k1':(-1, 'k'),
         '1i':( 1, 'i'),
         'ii':( 1, '1'),
         'ji':( 1, 'k'),
         'ki':(-1, 'j'),
         '1j':( 1, 'j'),
         'ij':(-1, 'k'),
         'jj':( 1, '1'),
         'kj':( 1, 'i'),
         '1k':( 1, 'k'),
         'ik':( 1, 'j'),
         'jk':(-1, 'i'),
         'kk':( 1, '1'),
        }

def ra(x, y):
    if x == None:
        return (1, y)
    if y == None:
        return (1, x)
    if len(y) == 1:
        y = (1, y)
    if len(x) == 1:
        x = (1, x)
    o = rule1[x[1]+y[1]]
    s = x[0]*y[0]*o[0]
    return (s, o[1])
    
def lr(x, y):
    if len(x) == 1:
        x = (1, x)
    o = rule2[x[1]+y[1]]
    s = x[0]*y[0]*o[0]
    return (s, o[1])
    
def do(s, length):
    if length<2:
        return False
    if length==3:
        return s=='ijk'
    d = None
    p2 =[]
    for i in reversed(range(length)):
        d = ra(s[i%len(s)], d)
        if d[0] == 1 and d[1] == 'k':
            p2.append(i)
    if len(p2) == 0:
        return False
    a = None
    for i in range(length-2):
        a = ra(a,s[i%len(s)])
        d = lr(s[i%len(s)], d)
        if a[0] == 1 and a[1] == 'i':
            b = None
            c = (d[0], d[1])
            for j in range(i, max(p2)):
                b = ra(b, s[j%len(s)])
                c = lr(s[j%len(s)], c)
                if b[0] == 1 and b[1] == 'j' and c[0] == 1 and c[1] == 'k':
                    return True
    return False
        

for i in range(num_of_case):
    line = raw_input().split(' ')
    X = int(line[1])
    line = raw_input()
    o = do(line, len(line)*X)
    if o:
        print("Case #%d: %s"% (i+1, 'YES'))
    else:
        print("Case #%d: %s"% (i+1, 'NO'))