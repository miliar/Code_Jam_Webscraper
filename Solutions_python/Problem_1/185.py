#save the universe

times = -1

def choose_engine(Engines,Queries,beg):
    global times
    temp = 0
    times += 1
    left = Queries[beg:]
    for engine in Engines:
        if engine not in left:
            return engine,None
        else:
            tmp = Queries.index(engine,beg)
            if tmp > temp:
                temp = tmp
    return Queries[temp],temp

if __name__ == '__main__':
    infile = open('input.in')
    outfile = open('output.out','w')
    case = int(infile.readline())
    for x in range(case):
        num_eng = int(infile.readline())
        Engines = [];Queries = []
        for i in range(num_eng):
            Engines.append(infile.readline())
        num_que = int(infile.readline())
        for i in range(num_que):
            Queries.append(infile.readline())
        beg = 0
        while beg != None:
            beg = choose_engine(Engines,Queries,beg)[1]
        outfile.write('Case #%d: %d\n'%((x + 1),times))
        times = -1
    infile.close()
    outfile.close()
        
