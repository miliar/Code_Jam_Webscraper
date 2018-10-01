for c in range(1,input()+1):

    a,b = raw_input().split()

    ia = int(a)
    ib = int(b)

    d={}
    for i in range(ia,ib+1):
        ai = str(i)
        l = len(ai)
        for j in range(1,l):
            t = ai[j:l]+ai[0:j]
            if a < t < b and t != ai:
                d[tuple(sorted((ai,t)))] = 1

    print"Case #%d:"%c, len(d)
