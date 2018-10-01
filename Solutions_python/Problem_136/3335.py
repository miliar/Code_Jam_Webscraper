num_cases = int(input())
for i in range(1, num_cases+1):
    ln = input()
    c = float(ln.split(" ")[0])
    f = float(ln.split(" ")[1])
    x = float(ln.split(" ")[2])

    t = float("inf")
    tnew = x/2
    tfarms = 0
    n = 0
    while tnew < t:
        t = tnew
        tfarms = tfarms + c/(2+n*f)
        n = n+1
        tnew = x/(2+n*f) + tfarms

    print("Case #"+str(i)+": "+str(t))
