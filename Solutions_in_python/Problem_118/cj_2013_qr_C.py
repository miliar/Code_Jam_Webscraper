'''
Created on Apr 12, 2013

@author: Andrew
'''

sample = '''3
1 4
10 120
100 100000000000000
'''.split('\n')

sample_o = '''Case #1: 2
Case #2: 0
Case #3: 2'''.split('\n')

def raw_input_test():
    global sample
    if len(sample) == 0:
        return ''
    ret = sample[0]
    sample = sample[1:]
    return ret

def _print(x):
    print x

def print_test(x):
    global sample_o
    s = sample_o[0]
    #if s != x: print "ERROR"
    sample_o = sample_o[1:]
    print x

getline = raw_input
printline = _print

#getline = raw_input_test
#printline = print_test

import math

def reverse(x):
    x = [y for y in x]
    x.reverse()
    return x

def get_fs(U):
    # Find sqrt of number
    SU = int(math.sqrt(U))
    
    if SU < 10:
        return 
    
    # Now find how many fair numbers are below SU
    N = int(math.log10(SU)) + 1 # digits in SU
    
    
    digits = map(int, list(str(SU)))
    
    left = digits[:(len(digits) + 1) / 2]
    right = digits[(len(digits) + 1) / 2:]
    ls = int(''.join(map(str,left)))
    rs = int(''.join(map(str,right)))
    print left,right
    print ls,rs
    
    candofirst = left[-1] <= right[0]
    remaining = ls - 1
    if candofirst:
        remaining += 1
     
    restoftens = 10**((N - 1) / 2) * 9
    
    result = remaining + restoftens
    
    return result

def fs(A, B):
    return get_fs(B) - get_fs(A - 1)


def checkfs(xs):
    s = str(xs)
    for x in xrange(len(s)/2):
        if s[x] != s[len(s) - x - 1]:
            return False
    return True

def fsiter(A, B):
    sa = int(math.sqrt(A))
    sb = int(math.sqrt(B))
    
    AU = int(math.log10(sa) + 2) / 2
    AU = 10**(AU - 1)
    x = AU
    
    LU = int(math.log10(sb) + 2) / 2
    LU = 10**LU
    if LU == 1:
        LU = 10
    
    #print 'sa,sb',sa,sb
    #print 'x',x,LU
    
    count = 0
    while x <= LU:
        s = str(x)
        h = s[:len(s)-1]
        
        y =  s + ''.join(reverse(s)) 
        z = s + ''.join(reverse(h))
        
        yi = int(y)
        zi = int(z)
        
        ys = yi**2
        zs = zi**2
        if ys <= B and ys >= A and checkfs(ys):
            #print 'y',y
            count += 1
        if zs <= B and zs >= A and checkfs(zs):
            #print 'z',z
            count += 1
        #print y,z
        x += 1
    return count

def fsiter2(B):
    
    sb = int(math.sqrt(B))
    
    x = 1
    
    LU = int(math.log10(sb) + 2) / 2
    LU = 10**LU
    
    results = []
    
    while x <= LU:
        s = str(x)
        h = s[:len(s)-1]
        
        y =  s + ''.join(reverse(s)) 
        z = s + ''.join(reverse(h))
        
        yi = int(y)
        zi = int(z)
        
        ys = yi**2
        zs = zi**2
        if checkfs(ys):
            results.append(ys)
            print math.log10(ys),ys
        if checkfs(zs):
            
            results.append(zs)
            print math.log10(zs),zs
        x += 1
    return results

def fsiter3(B):
    
    sb = 10**50
    
    x = 1
    
    #LU = int(math.log10(sb) + 2) / 2
    #LU = 10**LU
    
    LU = 10**25
    
    results = []
    
    while x <= LU:
        s = str(x)
        h = s[:len(s)-1]
        
        y =  s + ''.join(reverse(s)) 
        z = s + ''.join(reverse(h))
        
        yi = int(y)
        zi = int(z)
        
        ys = yi**2
        zs = zi**2
        if checkfs(ys):
            results.append(ys)
            print math.log10(ys),ys
        if checkfs(zs):
            
            results.append(zs)
            print math.log10(zs),zs
        x += 1
    return results

def countfs(fs, A, B):
    x = 0
    count = 0
    while x < len(fs) and fs[x] < A:
        x += 1
    while x < len(fs) and fs[x] <= B:
        count += 1
        x += 1
    return count 

    
def constraint(*args):
    return 2*sum([x*x for x in args]) < 10

def constraint2(*args):    
    return 2*sum([x*x for x in args]) - args[-1]**2 < 10

import itertools

def derp(x):
    return x[1:]

def next_permutation(seq, pred=cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""
    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
    if not seq:
        raise StopIteration
    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")
    first = 0
    last = len(seq)
    seq = seq[:]
    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq
    if last == 1:
        raise StopIteration
    while True:
        next = last - 1
        while True:
            # Step 1.
            next1 = next
            next -= 1
            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                # Step 3.
                reverse(seq, next1, last)
                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration


def genfs(N):
    results = []
    for n in xrange(0,N):
        #print 'n',n
        # If d0 is one, 
        # we can choose up to 3 other digits to be 1
        # M: We can choose the middle digit to be 2, and pick up to 1 more digit to be 1
        for y in range(4):
            rdigits = ['0'] * (n)
            x = 0
            while x < len(rdigits) and x < y:
                rdigits[(n - 1) - x] = '1'
                x += 1
            
            
            perms = [x for x in next_permutation(rdigits)] + [rdigits]
            
            #print rdigits
            #print perms
            #print
            perms2 = [['1'] + list(tu) + reverse(list(tu)) + ['1'] for tu in perms]
            perms3 = [['1'] + list(tu) + derp(reverse(list(tu))) + ['1'] for tu in perms]
            
            perms4 = [['1'] + list(tu) + ['1'] + reverse(list(tu)) + ['1'] for tu in perms]
            results += perms4
            #print perms3
            results += perms2
            results += perms3
            
            if x == len(rdigits): break
        
        # Special middle case
        rdigits = ['0'] * (n - 1)
        results += [['1'] + rdigits + ['2'] + rdigits + ['1']]
        if len(rdigits)> 0:
            rdigits[-1] = '1'
        
        perms = [x for x in next_permutation(rdigits)] + [rdigits]
        perms = [['1'] + list(tu) + ['2'] + reverse(list(tu)) + ['1'] for tu in perms]
        results += perms
        
        
        # If d0 is two,
        # everything else 0
        # M: We can choose the middle to be 1, everything else 0
        #print n,[2] + [0] * (2*n) + [2]
        results.append(['2'] + ['0'] * (2*n) + ['2'])
        
        #middle case
        f = ['0'] * (n - 1)
        results.append(['2'] + f +  ['1'] + f  + ['2'])
        results.append(['2'] + f +  ['0'] + f  + ['2'])
    results = [int(''.join(x)) for x in results]
    results = list(set(results))
    results = sorted(results)
    
    return results

def genfs2():
    x = 0
    while x < 3**25:
        
        x += 1
#fs = sorted(fsiter2(10**100))
fs = [1, 2, 3] + genfs(26)
fs = [x**2 for x in fs]
#for x in fs: print x
# print countfs(fs, 1, 4)
# print countfs(fs, 10, 120)
# print countfs(fs, 100, 1000)
#exit()

#fs =[1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L, 100000020000001L, 100220141022001L, 102012040210201L, 102234363432201L, 121000242000121L, 121242363242121L, 123212464212321L, 123456787654321L, 400000080000004L, 10000000200000001L, 10002000300020001L, 10004000600040001L, 10020210401202001L, 10022212521222001L, 10024214841242001L, 10201020402010201L, 10203040504030201L, 10205060806050201L, 10221432623412201L, 10223454745432201L, 12100002420000121L, 12102202520220121L, 12104402820440121L, 12122232623222121L, 12124434743442121L, 12321024642012321L, 12323244744232321L, 12343456865434321L, 12345678987654321L, 40000000800000004L, 40004000900040004L, 1000000002000000001L, 1000220014100220001L, 1002003004003002001L, 1002223236323222001L, 1020100204020010201L, 1020322416142230201L, 1022123226223212201L, 1022345658565432201L, 1210000024200000121L, 1210242036302420121L, 1212203226223022121L, 1212445458545442121L, 1232100246420012321L, 1232344458544432321L, 1234323468643234321L, 4000000008000000004L, 100000000020000000001L, 10000000000200000000001L]


#for x in xrange(1,100):
#print fsiter(1,x)

#print fsiter(1,4)

#print "done"
#print get_fs(120)
#print fs(10, 120)
#exit()


def isapal(xs):
    s = str(xs).replace('L','')
    ispal = True
    for y in range(len(s) / 2):
        if s[y] != s[(y+1)*-1]:
            ispal = False
            break
    return ispal 
def brute(A, B):
    sa = int(math.sqrt(A))
    sb = int(math.sqrt(B))
    
    numfs = 0
    for x in xrange(sa, sb+1):
        xs = x**2
        if xs < A:
            continue
        
        if isapal(x) and isapal(xs):
            numfs += 1
            #print x,xs
    return numfs


num_cases = int(getline())

for case_num in xrange(1,num_cases + 1):
    A, B = map(int, getline().strip().split(' '))
    #print A,B
    
    #msg = brute(A, B)
    #msg = fsiter(A,B)
    msg = countfs(fs, A, B)
    #assert msg == msg2
    printline("Case #{0}: {1}".format(case_num, msg))