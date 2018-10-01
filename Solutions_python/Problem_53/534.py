def p2d(tab):
    for e in tab:
        print(e)

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    for test in range(N):
        total = 'OFF'
        l = fin.readline().replace("\n", "")
        n, k = (int(v) for v in l.split(" ")) 
                
        if k == 0 or k < n: pass
        elif n == 1:
            if k % 2 == 1: total = 'ON'
        else:
            print n, k
            sn1 = 2**n-1
            snn = sn1+1
            #print sn1, snn

            if k < sn1: pass
            elif k == sn1: total = 'ON'
            else:
                k -= sn1
                if k % snn == 0: total = 'ON' 
                            
        sol = "Case #" + str(test+1) + ": " + str(total) + "\n"
        print(sol)
        fout.write(sol)
        