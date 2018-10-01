with open('A-small-attempt0.in', 'r') as infile:
    t = infile.readline()
    o = []
    for i in range(int(t.rstrip())):
        r = int(infile.readline().rstrip())
        r1 = infile.readline().rstrip().split()
        r2 = infile.readline().rstrip().split()
        r3 = infile.readline().rstrip().split()
        r4 = infile.readline().rstrip().split()
        g = [r1,r2,r3,r4]
        a1 = g[r-1]
        r = int(infile.readline().rstrip())
        r1 = infile.readline().rstrip().split()
        r2 = infile.readline().rstrip().split()
        r3 = infile.readline().rstrip().split()
        r4 = infile.readline().rstrip().split()
        g = [r1,r2,r3,r4]
        a2 = g[r-1]
        b = False
        output = ''
        for i in a1:
            if i in a2:
                if b:
                    output = 'Bad magician!'
                    break
                else:
                    b = True
                    output = str(i)
        if not output:
            output = 'Volunteer cheated!'
        o.append(output)

with open('A.out', 'w') as outfile:
    outfile.write('\n'.join(['Case #' + str(n+1) + ': ' + ans for n,ans in enumerate(o)]))
    
    
