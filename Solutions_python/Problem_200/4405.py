with open("output.txt", "wt") as fo:
    with open("B-large.in", "rt") as fi:
        t = int(fi.readline())
        for i in range(t):
            n = list(fi.readline().strip('\n'))
            for j in range(len(n)-1,0,-1):
                if int(n[j]) < int(n[j-1]):
                    n[j:] = ('9' for k in range(j,len(n)))
                    n[j-1] = int(n[j-1]) - 1
            fo.write("Case #%d: %s" %(i+1,"".join(map(str,n)).lstrip('0')))
            fo.write('\n')
    fi.close()
fo.close()