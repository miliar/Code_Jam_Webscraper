T = int(raw_input())
for i in range(T):
    line = raw_input()
    a, b, k = line.split()
    a = int(a)
    b = int(b)
    k = int(k)
    win = 0
    for x in range(a):
        for y in range(b):
            if x&y<k:
                win+=1
    print 'Case #'+str(i+1)+': '+str(win)
