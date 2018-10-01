n = int(raw_input())

for i in xrange(0,n):
    parts = [int(m) for m in raw_input().split()]
    N = parts[0]
    S = parts[1]
    p = parts[2]
    numbers = parts[3:]
    numbers.sort()
    numbers.reverse()
    counter = 0
    while S >= 0 and counter < N:
        if numbers[counter] == 0:
            if p==0: counter += 1
            else: break
        elif numbers[counter] >= 3 * p - 2:
            counter += 1
        elif numbers[counter] >= 3*p - 4:
            if S>0:S -= 1
            else: break
            counter += 1
        else:
            break
    
    print "Case #%d: %d" % (i+1,counter)
