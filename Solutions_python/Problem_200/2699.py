t = int(raw_input())                                   # test cases
for i in xrange(1, t+1):
    l = map(str, raw_input())
    n = len(l)
    status, signal = True, True
    temp = []
    start = 0
    for j in xrange(len(l)-1):
        if(l[j] == l[j+1] and signal == True):
            start = j
            signal = False
        elif(l[j] > l[j+1]):
            l = list(str(int(''.join(l[start:])) - int(''.join(l[start+1:]))))
            status = False    
            break
        elif(l[j] < l[j+1]):
            temp.extend(l[start:j+1])
            start = j+1
            signal = True
    if(status == False):
        temp.extend(list(str(int(''.join(l)) - 1)))
    else:
        temp.extend(l[start:])

    ans = int(''.join(temp))
    print "Case #{}: {}".format(i, ans)    