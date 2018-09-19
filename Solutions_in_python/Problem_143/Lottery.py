def lottery(filename):
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for test in range(0, testcases):
        A, B, K = (file.readline().strip('\n').split(' '))
        A = int(A)
        B = int(B)
        K = int(K)
        a = []
        b = []
        k = []
        tmp = []
        ans = []
        count = 0
        for i in range(A):
            a.append(bin(i))
        for j in range(B):
            b.append(bin(j))
        for i in range(K):
            k.append(i)
        for i in range(A):
            ta = a[i]
            for j in range(B):
                tb = b[j]
                if len(ta) < len(tb):
                	ta = '0b' + (len(tb)-len(ta))*'0' + ta[2:]
                if len(tb) < len(ta):
                	tb = '0b' + (len(ta)-len(tb))*'0' + tb[2:]
                temp = '0b'
                for var in range(2, len(ta)):
                    if ta[var] == '1' and tb[var] == '1':
                        temp += ('1')
                    else:
                        temp += ('0')
                tmp.append((int(temp,2), int(ta,2), int(tb,2)))
        for i in tmp:
            if i[0] in k:
                count += 1
        final = "Case #" + str(test+1) + ": " + str(count) +"\n"
        out.write(final)
        print(final)
        
