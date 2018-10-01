def find_n(x):
    return len(str(x))

def rotate(s):
    r = s[len(s)-1]+s[:len(s)-1]
    return r

x = int(raw_input().strip())
for c in range(x):
    ans = []
    bound = raw_input().strip().split()
    _min = int(bound[0])
    _max = int(bound[1])
    now = _min
    while(now < _max):
        n = find_n(now)
        test = str(now)
        for i in range(n-1):
            test = rotate(test)
            if(int(test) >= _min and int(test) <= _max and int(test) > now):
                ans.append((now,int(test)))
                #print now,test
        now += 1
    print 'Case #' + str(c+1) + ': ' + str(len(list(set(ans))))
