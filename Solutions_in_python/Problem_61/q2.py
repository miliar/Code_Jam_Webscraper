import operator
def factorial(num):
    return reduce(operator.mul, range(1, num + 1), 1) # the "1" initial value allows it to work for 0


def binomial(n, k):
    if n==0:
        return 1
    assert n>0 and isinstance(n, (int, long)) and isinstance(k, (int,
    long))
    if k < 0 or k > n:
        return 1
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n-k))

cache = dict()

def options_over(last, size):
    if(size==1):
        return 1;
    if(size>=last):
        return 0
    sum = 0;
    key = str(last) + ',' + str(size);
    
    if key in cache:
        return cache[key]
    
    diff = last - size;
    for i in range(1,diff+1):
        if(size-i==0):
            break
        sum = sum + (options_over(size,size - i)*binomial(last-size-1,i-1))
    
    cache[key] = sum
    
    return sum

def how_much(n):
    res = 0;
    for i in range(1,n):
        res = res + options_over(n,i)
    return res
 

#print options_over(8, 4)
#print how_much(6)

t = int(input())
       
for x in range(1,t+1):
    n = int(input())
    print "Case #%d: %d" % (x, how_much(n) % 100003)