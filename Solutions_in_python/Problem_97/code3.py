t = input("")
for i in range(t):
    z = raw_input("")
    y = z.split(" ")
    a = int(y[0])
    b = int(y[1])
    #a = input("")
    #b = input("")
    l = []
    x = []
    for j in range(a, b + 1):
        s = str(j)
        l.append(s)
        for k in range(len(s)-1):
            s = s[1:] + s[0]
            if int(s) >= a and int(s) <= b and not int(s) == j:
                if s in l:
                    if s not in x:
                        x.append(s)
                else:
                    l.append(s)
    x.sort()
    #print x
    print 'Case #' + str(i+1) + ': '+ str(len(x))
    #print "-------------------------------------------------------"
