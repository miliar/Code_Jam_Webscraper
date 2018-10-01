

class MagicTrick(object):

    def getData(self, fin):
        _r = fin.readline().strip(' \n')
        print 'row'
        print type(_r)
        print repr(_r)
        r = int(_r)
        grid = []
        for i in range(4):
            row = fin.readline().strip(' \n').split(' ')
            grid.append(row)
        return (r, grid)
    
    def getDict(self, r, grid):
        d = dict()
        for n in grid[r - 1]:
            d[n] = 0
        return d

    def solve(self):
        fin = open('input', 'r')
        fout = open('output', 'w')
        T = fin.readline().strip(' \n')
        print T
        T = int(T)
        for idx in range(T):
            (r0, grid0) = self.getData(fin)
            (r1, grid1) = self.getData(fin)
            d0 = self.getDict(r0, grid0)
            d1 = self.getDict(r1, grid1)
            fout.write('Case #%s: ' % str(idx + 1))
            cnt = 0
            ans = 0
            for k in d0:
                if d1.has_key(k):
                    cnt += 1
                    if cnt > 1:
                        ans = -1
                        break
                    ans = k
            if ans == 0:
                fout.write('Volunteer cheated!')
            elif ans == -1:
                fout.write('Bad magician!')
            else:
                fout.write(ans)
            fout.write('\n')
        fin.close()
        fout.close()

if __name__ == '__main__':
    handle = MagicTrick()
    handle.solve()
