def snapperChain( N, K, i ):
    a = (K+1)%( pow(2,N) )
    output = ""
    if a == 0:
        output = "ON"
    else:
        output = "OFF"
    return "Case #%d: %s\n" % (i, output)


snapperChain( 4, 47, 4)
fp = open("A-large.in", 'r')
fout = open("A-large.out", 'w')
T = int(fp.readline())
for i in range(1, T+1):
    N, K = fp.readline().split()
    N = int(N)
    K = int(K)
    fout.write(snapperChain(N, K, i))
fp.close()
fout.close()
