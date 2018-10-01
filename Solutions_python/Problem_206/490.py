[cases] = [int(x) for x in raw_input().strip().split()]
out = open('output.txt', 'w')

for case in range(cases):
    # solving logic goes here
    (d, n) = [int(x) for x in raw_input().strip().split()]
    maxtime = None
    for i in range(n):
        (k, s) = [int(x) for x in raw_input().strip().split()]
        t = (d - k) * 1.0 / s
        if maxtime is None or t > maxtime:
            maxtime = t

    s = "Case #"+str(case+1)+": "+str(d / maxtime)+'\n'
    out.write(s)
    print(s)
