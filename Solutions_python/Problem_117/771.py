

class Lawn(object):
    """docstring for Lawn"""
    def __init__(self, mat, n, m):
        super(Lawn, self).__init__()
        self.mat = mat
        self.n = n
        self.m = m
        # self.min_rows = [self.min_row(i) for i in range(0,self.n)]
        self.max_rows = [self.max_row(i) for i in range(0,self.n)]
        # self.min_cols = [self.min_col(i) for i in range(0,self.m)]
        self.max_cols = [self.max_col(i) for i in range(0,self.m)]

        
    def get(self,i,j):
        return self.mat[i][j]

    def max_row(self,i):
        return max(self.mat[i])
    def min_row(self,i):
        return min(self.mat[i])

    def max_col(self,i):
        return max([self.get(j,i) for j in range(0,self.n)])
    def min_col(self,i):
        return min([self.get(j,i) for j in range(0,self.n)])


class Problem2(object):
    """docstring for Problem2"""
    def __init__(self, lawn):
        super(Problem2, self).__init__()
        self.lawn = lawn

    def solve(self):
        for i in range(0,self.lawn.n):
            for j in range(0, self.lawn.m):
                if min([self.lawn.max_rows[i], self.lawn.max_cols[j]]) > self.lawn.get(i,j):
                    return 'NO'
        return 'YES'
        

def main():
    with open('B-large.in','r') as fn:
        n = int(fn.readline()[:-1])
        for i in range(1,n+1):
            mat = []
            pair = [int(k) for k in fn.readline()[:-1].split(' ')]
            n,m = pair[0],pair[1]
            for _ in range(0,n):
                line = fn.readline()
                if line[-1] is '\n':
                    line = line[:-1]
                mat.append([int(k) for k in line.split(' ')])
            print 'Case #{0}: {1}'.format(i, Problem2(Lawn(mat,n,m)).solve())
    

if __name__ == '__main__':
    main()
