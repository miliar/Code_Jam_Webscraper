with open("A.in") as infile:
    with open("A.out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            N, K = (int(s) for s in infile.readline().split())
            # Perform all nessesary calculation
            if ((K+1) % (pow(2,N))) == 0: out = "ON"
            else: out = "OFF"
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=out))
print("Ready")
