t = input()
for z in xrange(1,t+1):
    n = input()
    naomi = sorted(map(float,raw_input().split()) ,reverse=True)
    ken = sorted(map(float,raw_input().split()), reverse = True)
    #table = [False]*10**6
    #for w in xrange(n):
    #    table[int(naomi[w]*10**5)] = True
    #    table[int(ken[w]*10**5)] = True
    war = 0
    dwar = 0
    x,y = n-1,n-1
    cc = 0
    while y>=0:
        if naomi[x] > ken[y]:
            y-=1
        else:
            x-=1
            y-=1
    war = x+1
    xf = 0
    xb = n-1 
    y = 0
    while y<n:
        if naomi[xf]>ken[y]:
            xf+=1
            y+=1
        else:
            xb-=1
            y+=1
            """
            if table[int((ken[y]-0.00001)*10**5)]:
                y+=1
            else:
                y+=1
                xb-=1
            continue
            """
    dwar = xf
    #print naomi
    #print ken
    print ("Case #%d: %d %d") % (z,dwar,war)
