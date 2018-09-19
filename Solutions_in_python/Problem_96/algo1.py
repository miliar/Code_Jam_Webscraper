def main(filename):

    try:
        infile = open(filename+'.in', 'r')
        outfile = open(filename+'.out', 'w')
    except IOError:
        return

    T = int(infile.readline())

    for case in range(T):
        splitline = [char for char in infile.readline().strip('\n').split()]
        N = int(splitline[0])
        S = int(splitline[1])
        p = int(splitline[2])
        points = [int(each) for each in splitline[3:]]
        assert len(points) == N

        mintotal = p*3 - 3
        ans = 0
        for each in points:
            if each > mintotal and each <> 0:
                ans = ans + 1
            elif each > mintotal - 2 and each <> 0:
                if S > 0:
                    ans = ans + 1
                    S = S - 1
            elif p == 0 and each == 0:
                ans = ans + 1

        #if S > 0:
        #    print "Case {0}: S = {1}".format(case+1, S)

        outfile.write("Case #{0}: {1}\n".format(case+1, ans))

    infile.close()
    outfile.close()

if __name__ == '__main__':
    main('test')
    main('small')
    main('large')
