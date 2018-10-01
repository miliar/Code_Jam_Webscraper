import itertools

casename = 'large'

def solve():
    fi = open('bot_'+casename+'_in.txt','r')
    fo = open('bot_'+casename+'_out.txt','w')
    T = int(fi.readline())
    for t in xrange(1,T+1):
        parts = fi.readline().split()
        N = int(parts[0])
        clist = [parts[1+i*2] for i in xrange(N)]
        poslist = [int(parts[2+i*2]) for i in xrange(N)]

        opos,otime = 1,0
        bpos,btime = 1,0
        spent = 0

        for (color,pos) in itertools.izip(clist,poslist):
            if color=='B':
                btime = max(btime+abs(pos-bpos),spent)+1
                spent = max(spent,btime)
                bpos = pos
            if color=='O':
                otime = max(otime+abs(pos-opos),spent)+1
                spent = max(spent,otime)
                opos = pos
        fo.write("Case #%d: %d\n"%(t,spent))
    fi.close()
    fo.close()
        
