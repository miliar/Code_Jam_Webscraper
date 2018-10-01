import itertools

def pure(a, n):
    if n == 1:
        return True
    i = 1
    for x in a:
        if x > n:
            return False
        if x == n:
            return pure(a, i)
        i += 1
    return False
	
def combos(n):
    b = [()]
    for i in range(1,n):
        for j in itertools.combinations(range(2,n+1), i):
            b.append(j)
    return b
    
def count(n):
    count = 0
    for c in combos(n-1):
        check = c + (n,)
        if pure(check, n):
            #print check, 'YES'
            count += 1
    return count


#for i in range(2, 26):
#    c = count(i)
#    print c, ',', '# ', i

arr = [
0, #0
0, #1
1 , #  2
2 , #  3
3 , #  4
5 , #  5
8 , #  6
14 , #  7
24 , #  8
43 , #  9
77 , #  10
140 , #  11
256 , #  12
472 , #  13
874 , #  14
1628 , #  15
3045 , #  16
5719 , #  17
10780 , #  18
20388 , #  19
38674 , #  20
73562 , #  21
140268 , #  22
268066 , #  23
513350 , #  24
984911 , #  25
]

data = open('C-small-attempt0.in').read().split()
data.reverse()
T = int(data.pop())
for t in range(1,T+1):
    print 'Case #{0}: {1}'.format(t, arr[int(data.pop())] % 100003)
