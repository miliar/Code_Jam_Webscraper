
def processline(line):
    return int(line[0:2])*60 + int(line[3:5]), int(line[6:8])*60+int(line[9:11])

def train(filename):
    fin = open(filename+'.in','r')
    fout = open(filename+'.out','w')

    N = int(fin.readline())
    for case in range(N):
        T = int(fin.readline())
        nanb = fin.readline()
        nanb = nanb.split()
        NA, NB = int(nanb[0]), int(nanb[1])
        station_a = list(0 for i in range(60*24))
        station_b = list(0 for i in range(60*24))
        for a in range(NA):
            (a_start, b_arrive) = processline(fin.readline())
            station_a[a_start] -= 1
            if b_arrive+T<60*24 :
                station_b[b_arrive+T]+=1
        for b in range(NB):
            (b_start, a_arrive) = processline(fin.readline())
            station_b[b_start]-=1
            if a_arrive+T<60*24 :
                station_a[a_arrive+T]+=1
        ra, rb = 0, 0
        sa, sb = 0, 0
        for i in range(60*24):
            sa+=station_a[i]
            sb+=station_b[i]
            ra=min(ra, sa)
            rb=min(rb, sb)
        print >>fout, 'Case #%d: %d %d' % (case+1, -ra, -rb)
    fout.close()
    fin.close()

train('B-large')

