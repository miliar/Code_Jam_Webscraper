if __name__ == '__main__':
    f = open('B-large.in')
    output = open('B-large.out', 'w')
    T = int(f.readline())
    for i in range(T):
        line = f.readline()
        l = line.split()
        l = [int(l[j]) for j in range(len(l))]
        num = l[0]
        surp = l[1]
        p = l[2]
        l = l[3:]
        poss = 0
        l.sort()
        l.reverse()
        for item in l:
            if item % 3 == 0:
                if item / 3 >= p:
                    poss += 1
                elif (item / 3 + 1 >= p) and (surp >= 1) and (item / 3) >= 1:
                    poss += 1
                    surp -= 1
            elif item % 3 == 1:
                if (item + 2) / 3 >= p:
                    poss += 1
            else:
                if (item + 1) / 3 >= p:
                    poss += 1
                elif ((item + 1) / 3 + 1 >= p) and (surp >= 1):
                    poss += 1
                    surp -= 1
        s = 'Case #%s: %s\n' %(i + 1, poss)
        output.write(s)
    f.close()
    output.close()
