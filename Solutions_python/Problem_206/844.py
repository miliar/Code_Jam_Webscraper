
def solve(representation):
    D, N, KS = representation
    print(D, N, KS)


    time = [(D-K)/S for K,S in KS]
    print(D/max(time))

    return D/max(time)



def getprob(content):
    D,N = (int(l) for l in content[0].split(' '))
    list = [line for line in content[1:1 + N]]
    del content[:1 + N]
    return D,N,list


def parseprob(prob):
    D, N, list=prob
    KS=[]
    KS = [line.split() for line in list]
    KS = [(int(a),int(b)) for a,b in KS]

    return D,N,KS


def readAndSolve():
    d = "C:\\Users\\dave\\Downloads\\"
    infile = "A-large.in"
    content = []
    with open(d + infile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    numprobs = int(content[0])
    del content[0]

    lines = []
    for pnum in range(numprobs):
        prob = getprob(content)
        representation = parseprob(prob)
        solved = solve(representation)
        str = 'Case #{}: {}'.format(pnum + 1, solved)
        print(str)
        lines.append(str)

    outfname = infile.replace(".in", ".out")
    outfile = "C:\\Users\\dave\\PycharmProjects\\codejam_2017_1b\\" + outfname
    f = open(outfile, 'w')
    print('\n'.join(lines), file=f)
    f.close()


readAndSolve()
