import sys

mappings = {
    '11': '1',
    '1i': 'i',
    '1j': 'j',
    '1k': 'k',
    'i1': 'i',
    'ii': '-1',
    'ij': 'k',
    'ik': '-j',
    'j1': 'j',
    'ji': '-k',
    'jj': '-1',
    'jk': 'i',
    'k1': 'k',
    'ki': 'j',
    'kj': '-i',
    'kk': '-1'
}

def input():
    T = int(sys.stdin.readline())
    for i in range(1,T+1,1):
        L,X = map(int, sys.stdin.readline().split())
        string = sys.stdin.readline().strip()
        print "Case #{}: {}".format(i,djikstra(L,X,string))

def djikstra(L,X,string):
    string *= X
    found = 0
    if string[0] == 'i':
        found = 1
        prod = 'i'
    else:
        prod = string[0]
    for i,s in enumerate(string[1:], start=1):
        if (found == 0 and prod == 'i'):
            found = 1
            prod = s
            continue
        if (found == 1 and prod == 'j'):
            found = 2
            prod = s
            continue
        if (found == 2 and prod == 'k'):
            found = 3
            prod = s
            continue
        if (found == 3 and prod == '1'):
            found = 4
            prod = s
            continue
        prod = mul(prod, s)

    print found
    if found == 3 or found == 4:
        return 'YES'
    else:
        return 'NO'



def mul(a,b):
    if a.startswith("-"):
        res = mappings[a[1:2]+b]
        if res.startswith("-"):
            return res
        else:
            return "-" + res
    else:
        return mappings[a+b]


input()