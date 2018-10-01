#casename = 'sample'
#casename = 'small'
casename = 'large'

def solve():
    fi = open('candy_'+casename+'_in.txt','r')
    fo = open('candy_'+casename+'_out.txt','w')
    T = int(fi.readline())
    for t in xrange(1,T+1):
        N = int(fi.readline())
        c = map(int,fi.readline().strip().split())
        psum = reduce(lambda x,y:x^y,c)        
        fo.write("Case #%d: %s\n"%(t,[str(sum(c)-min(c)),'NO'][psum!=0]))
    fi.close()
    fo.close()
        
