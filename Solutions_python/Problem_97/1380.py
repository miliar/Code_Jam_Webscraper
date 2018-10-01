for e in enumerate([x.split(' ') for x in input().split('\n')[1:]]):
    count = 0
    A, B = int(e[1][0]), int(e[1][1])
    for n in range(A, B+1):
        ns = str(n)
        setm = set()
        for mspl in range(1, len(str(n))):
            ms = ns[mspl:]+ns[0:mspl]
            if ms[0] == '0': continue
            m = int(ms)
            if m > n and A <= m <= B and m not in setm:
                setm.add(m)
                count += 1
    print("Case #" + str(e[0]+1) + ": " + str(count))
