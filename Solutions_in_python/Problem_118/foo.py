li = [1,4,9]

LIM = 110

def gen1(rem, cnt):
    if rem == 0: 
        yield ''
        return

    if cnt > 0:
        for x in gen1(rem-1, cnt-1):
            yield '1'+x

    for x in gen1(rem-1, cnt):
        yield '0'+x

#x + x + 2 <= LIM/2
#x <= (LIM/2 - 2) / 2
for y in xrange((LIM/2 - 2)/2 + 1):
    for x in gen1(y, 3):
        li.append(int('1'+x+x[::-1]+'1')**2)

#x + x + 3 < LIM
#
for y in xrange((LIM/2 - 3)/2 + 1):
    for x in gen1(y, 3):
        li.append(int('1'+x+'0'+x[::-1]+'1')**2)
        li.append(int('1'+x+'1'+x[::-1]+'1')**2)

for y in xrange((LIM/2 - 3)/2 + 1):
    for x in gen1(y, 1):
        li.append(int('1'+x+'2'+x[::-1]+'1')**2)

for size in xrange(0, (LIM/2 - 3)/2 + 1):
    li.append(int('2'+ '0'*size + '0'*size + '2')**2)
    li.append(int('2'+ '0'*size + '0' + '0'*size + '2')**2)
    li.append(int('2'+ '0'*size + '1' + '0'*size + '2')**2)

li = list(set(li))
li.sort()


# def pa(x):
#     return str(x) == str(x)[::-1]
# 
# li = []
# for x in xrange(1, 10**7+1):
#     if pa(x) and pa(x**2): li.append(x**2)
# 
# print li[:36]
def upto(n):
    st = -1
    end = len(li)-1
    while (st < end):
        mid = (st+end+1)/2
        if li[mid] <= n: st = mid
        else: end = mid-1
    return st+1

T = int(raw_input())
for y in xrange(T):
    a,b = map(int,raw_input().split())
    print "Case #%s:" % (y+1), upto(b)-upto(a-1)





