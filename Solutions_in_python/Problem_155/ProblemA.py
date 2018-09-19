if __name__ == '__main__':
    f = open('A-large-practice.in')
    t = int(f.readline())
    # t = int(raw_input("T="))
    for i in range(t):
        line = f.readline()
        s_max = int(line.split()[0])
        # s_max = int(raw_input("Smax="))
        current = 0
        more = 0
        string = line.split()[1]
        # string = raw_input("string=")
        for j in range(s_max + 1):
            s = string[j]
            if int(string[j]) > 0 and j > current + more:
                more = j - current
            current += int(string[j])
        print "Case #{0}: {1}".format(i+1, more)