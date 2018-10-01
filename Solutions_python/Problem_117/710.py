class Garden:

    def __init__(self, n, m):
        self.lawn = []
        self.N = n
        self.M = m
        self.init_h = 100
        self.test_lawn = [[self.init_h]*M]*N

    def add_row(self, lst):
        self.lawn.append(lst)

    def get_row(self, i):
        return self.lawn[i]

    def get_col(self, i):
        ret = []
        for j in range(0,self.N):
            ret.append(self.lawn[j][i])

        return ret

    def get_test_row(self, i):
        return self.test_lawn[i]

    def get_test_col(self, i):
        ret = []
        for j in range(0,self.N):
            ret.append(self.test_lawn[j][i])

        return ret

    def write_row(self, i, row):
        self.lawn[i] = [min(self.lawn[i][j], row[j]) for j in range(0, M)]

    def write_test_row(self, i, row):
        self.test_lawn[i] = [min(self.test_lawn[i][j], row[j]) for j in range(0, M)]

    def write_col(self, i, col):
        for j in range(0,self.N):
            self.lawn[j][i] = min(self.lawn[j][i], col[j])

    def write_test_col(self, i, col):
        for j in range(0,self.N):
            self.test_lawn[j][i] = min(self.test_lawn[j][i], col[j])

    def clean_garden(self):
        for i in range(0, N):
            for j in range(0, M):
                row = self.get_row(i)
                col = self.get_col(j)
                if(max(row) is self.lawn[i][j] or max(col) is self.lawn[i][j]):
                    if(max(row) is self.lawn[i][j]):
                        self.write_test_row(i, [max(row)]*self.M)
                    else:
                        self.write_test_col(j, [max(col)]*self.N)
                    # print(self.test_lawn)
                else:
                    return False

        return self.lawn == self.test_lawn


num_cases = int(raw_input())

for case in range(1, num_cases + 1):
    dim = (raw_input()).split(" ")
    N = int(dim[0])
    M = int(dim[1])

    garden = Garden(N, M)

    for i in range(0, N):
        row = [int(r) for r in (raw_input()).split(" ")]
        garden.add_row(row)

    if(garden.clean_garden()):
        print("Case #"+str(case)+": YES")
    else:
        print("Case #"+str(case)+": NO")