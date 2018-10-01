doc = open("C-large.in").read()

lines = doc.split("\n")
T = int(lines[0])

def function(n, k):

    maxi, mini = n, k
    tmp = k - 1
    count = 0

    while True:
        tmp -= 2**count
        if(tmp < 0): 
            break
        count += 1
    c = 0
    for i in range(count):
        c += 2**i
    
    n -= c
    k -= c
    
    temp = 2**count
    
    large = n - temp * int(n / temp)
    small = temp - large
    
    if k <= large:
        size = int(n / temp) + 1
    else:
        size = int(n / temp)
    
    maxi = int(size / 2)
    mini = int((size - 1) / 2)
        
    return maxi, mini

for i in range(1, T+1):
    n, k = lines[i].split(" ")
    n = int(n)
    k = int(k)

    max_result, min_result = function(n, k)
    
    print("Case #{0}: {1} {2}".format(i, max_result, min_result))



