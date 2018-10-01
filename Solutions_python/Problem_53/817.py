# usage : snapper.py problem_instance.in

class Snapper:

    def __init__(self,argv):
        self.argv = argv
        self.number = 0
        self.case = 0
        self.out = ''
        self.data = []
        self.input()

    def input(self):
        f = open(self.argv,'r')
        self.lines = f.readlines()
        f.close()
        self.number = int(self.lines[0])
        self.lines = self.lines[1:]
        for i in range(0, len(self.lines)):
            self.data.append(self.lines[i].split(' '))

    def output(self):
        sys.stdout.write(self.out)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(self.out)
        f.close()

    def solve(self):
        res = 0
        comp = 0
        N = int(self.data[self.case][0])
        K = int(self.data[self.case][1])
        for i in range(1, N+1):
            if ((K-res)%(2**i) == 1) :
                res += (2**i)
                comp += 1
        if comp==N :
            self.out += 'Case #'+str(self.case+1)+': ON\n'
        else :
            self.out += 'Case #'+str(self.case+1)+': OFF\n'
        self.case += 1
    
    def Run(self):
        for i in range(0, self.number) :
            self.solve()
        self.output()

if __name__ == "__main__":
    import sys
    snapper = Snapper(sys.argv[1])
    snapper.Run()
    sys.exit(0)
