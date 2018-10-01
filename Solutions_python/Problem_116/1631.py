n = int(input())
for h in range(n):
    a = []
    for i in range(4):
        a.append(list(input()))
    r = input()    
    fl = 0
    ans = ''
    for i in range(4):
        if len(list(set(a[i]))) == 1 or (len(list(set(a[i]))) == 2 and sorted(list(set(a[i])))[1] =='T'):
            if list(set(a[i]))[0] != '.':
                fl = 1
                ans = sorted(list(set(a[i])))[0]
    b = []
    for i in range(4):
        x = []
        for j in range(4):
            x.append(a[j][i])
        b.append(x)
    for i in range(4):
        if len(list(set(b[i]))) == 1 or (len(list(set(b[i]))) == 2 and sorted(list(set(b[i])))[1] =='T'):
            if list(set(b[i]))[0] != '.':            
                fl = 1
                ans = sorted(list(set(b[i])))[0]        
    x = []
    for i in range(4):
        x.append(a[i][i])
    if len(list(set(x))) == 1 or (len(list(set(x))) == 2 and sorted(list(set(x)))[1] =='T'):
        if list(set(x))[0] != '.':
            fl = 1
            ans = sorted(list(set(x)))[0]
    x = []
    for i in range(4):
        x.append(a[3 - i][i])
    if len(list(set(x))) == 1 or (len(list(set(x))) == 2 and sorted(list(set(x)))[1] =='T'):
        if list(set(x))[0] != '.':
            fl = 1
            ans = sorted(list(set(x)))[0]         
    d = 1
    for i in range(4):
        for j in range(4):
            if a[i][j] == '.':
                d = 0
    if fl == 1:
        print('Case #',h+1,': ',ans,' won',sep = '')
    else:
        if d == 1:
            print('Case #',h+1,': Draw',sep = '')
        else:
            print('Case #',h+1,': Game has not completed',sep = '')