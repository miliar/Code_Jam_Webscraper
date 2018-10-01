fin = open("A-large.in", "r")
fout = open("A-large.out", "w")

T = int(fin.readline())

for t in xrange(T):
    N, K = [int(i) for i in fin.readline().split()]
    s = [int(i) for i in bin(K).lstrip("0b")[::-1]]
    if K == 0:
        on = False
    elif len(s) >= N:
        on = min(s[:N])
    else:
        on = False
    #print "Case #%i: %s" % (t + 1, "ON" if on else "OFF")
    fout.write("Case #%i: %s\n" % (t + 1, "ON" if on else "OFF"))

fin.close()
fout.close()

print "done"
