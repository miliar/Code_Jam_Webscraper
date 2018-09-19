def main():
    f = open('C-small.in', 'r')
    fOut = open('C-small.out', 'w')
    inp = f.readlines()
    cases = int(inp[0].replace('\n', ''))
    del inp[0]
    for i in range(cases):
        pos = i * 2
        line = inp[pos].replace('\n', '').split(' ')
        line2 = inp[pos+1].replace('\n', '').split(' ')
        r = int(line[0])
        k = int(line[1])
        n = int(line[2])
        groups = []
        for g in range(n):
            group = int(line2[g])
            groups.append(group)

        total = 0
        for t in range(r):
            people = 0
            index = 0
            while index < n and (people + groups[index]) <= k:
                people += groups[index]
                index += 1
            total += people
            l = groups[:index]
            groups[:index] = []
            groups += l

        result = 'Case #' + str(i+1) + ': ' + str(total)
        print result
        fOut.write(result + '\n')
    f.close()
    fOut.close()


if __name__ == '__main__':
    main()
