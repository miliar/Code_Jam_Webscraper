def print_2d(tab):
    for e in tab:
        print(e)


if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    for test in range(0, N):
        total = 0
        num = fin.readline().replace("\n", "")
        base = []
        val = []

        print(num)

        
        for q in num:
            val.append(q)
            if q not in base:
                base.append(q)
                
        if(len(base) > 1):
            base[0], base[1] = base[1], base[0]
        else:
            base[:0] = [0]
            
        #print(base)  
        #print("val", val)

        pow = 0
        for i in range(len(val)-1, -1, -1):            
            total += (len(base)**pow) * base.index(val[i])
            pow += 1


        #print("base", base)

        sol = "Case #" + str(test+1) + ": " + str(total) + "\n"
        print(sol)
        fout.write(sol)