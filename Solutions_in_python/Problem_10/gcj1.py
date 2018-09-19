
f = open("A-large.in")
out = open("output.txt",'w')
line = int(f.readline())
for case in range(1,line+1):
    p,k,l = [int(x) for x in f.readline().split()]
    keys_val = {}
    keys = []
    for v in [int(x) for x in f.readline().split()]:
        keys.append(v)
    keys.sort()
    keys = keys[::-1]
    tmp_k = k
    tmp_p = 1
    sum = 0
    for key in keys:
        sum += key*tmp_p
        tmp_k -= 1
        if tmp_k == 0:
            tmp_k = k
            tmp_p += 1
    out.write("Case #%d: %d\n" % (case,sum))
    print "Case #%d: %d" % (case,sum)