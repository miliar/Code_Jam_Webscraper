DEBUG = False

class Loader:
    def __init__(self,filename='data3.txt'):
        self.fp = open(filename)
        self.size = int(self.fp.readline().strip())
        self.pos = 0

    def run(self):
        case = 1
        for i in range(self.size):
            (r,t)= self.fp.readline().split()
            r = int(r)
            t = int(t)
#print 'run'
            myT = self.calculate(r,t)
            print 'Case #%d: %d'%(case,myT)
            case += 1
            
#print r,t,'============>',myT

    def calculate(self, r, t):
        sum = 0
        n = 1
        while sum <= t:
          sum = 2*n**2 + n*2*r - n
          n += 1
        return n-2
        '''
        sum = 0
        lastSum = sum
        n = 0
#print 'r=%d,maxArea=%d'%(r,3*t)
        while sum <= t:
          area = 2*r+4*n+1
          lastSum = sum
#print 'area=',str(area)+",currentArea=",str(sum)
          sum += area
#print 'now currentArea=',str(sum),',3*t=',str(3*t)
          n += 1
          '''
        return n-1

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 :
      filename = sys.argv[1]
    else:
      filename = 'data_a.txt'
    loader = Loader(filename)
    loader.run()
