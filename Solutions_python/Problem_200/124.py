T = int(raw_input())

for i in xrange(T):
    x = map(int, raw_input())
    j = 0
    while j < len(x)-1 and x[j] <= x[j+1]:
        j += 1
    if j == len(x) - 1:
        print 'Case #' + str(i+1) + ': ' + ''.join(map(str, x))
        continue
    k = j
    while k >= 0 and x[k] == x[j]:
        k -= 1
    x[k+1] -= 1
    for u in xrange(k+2, len(x)):
        x[u] = 9
    u = 0
    while x[u] == 0:
        u += 1
    print 'Case #' + str(i+1) + ': ' + ''.join(map(str, x[u:]))
    
    


#def check(x):
#    k = str(x)
#    for i in xrange(len(k)-1):
#        if k[i] > k[i+1]:
#            return False
#    return True
#
#while not check(T):
#    T -= 1;
#
#print T 
#


