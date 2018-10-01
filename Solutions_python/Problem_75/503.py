import sys

def magicka(combine, opposed, sequence):
    elements = {}
    prev = ''
    seq = ''
    for l in sequence:
        w = True
        while w:
            #print seq,l, elements
            w, seq, l = append( elements, seq, l, opposed, combine )
            #print w,seq,l
            if seq == '' and l == '':
                elements = {}
        #print seq
        seq += l
    return "[" + ", ".join(seq) + "]"
            
def append( elements, seq, l, opposed, combine):
    if len( seq ) == 0:
        #print "zero"
        return False, seq, l

    if l + seq[-1] in combine.keys():
        return True, seq[0:-1], combine[ l + seq[-1] ]

    if l not in opposed:
        return False, seq, l

    for a in opposed[l]:
        if a not in seq:
            continue
        else:
            return True, '', ''

    return False, seq, l

        

def premagicka( line ):
    l = line.split()
    indx = 0

    c = int( l[indx] )
    
    combine = {}
    for ci in range(c):
        ca, cb, cc = l[1 + ci]
        combine[ca + cb] = cc
        combine[cb + ca] = cc

    d = int( l[ c + 1] )
    opposed = {}
    for di in range(d):
        da, db = l[ 2 + c + di]
        if not da in opposed:
            opposed[da] = [db]
        else:
            opposed[da].append(db)

        if not db in opposed:
            opposed[db] = [da]
        else:
            opposed[db].append(da)

    combo = l[ c + d + 3 ]
    #print combine, opposed, combo
    return magicka( combine, opposed, combo )

t = sys.stdin.readline()

num = 0
for line in sys.stdin.readlines():
    num += 1
    print "Case #%s: %s" % (num, premagicka( line.strip() ) )
