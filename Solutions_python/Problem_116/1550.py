# -*- coding: utf-8 -*-
import gcj.base
import gcj.grid

IDX_GGLER_COUNT = 0
IDX_SURPRISING_COUNT = 1
IDX_P = 2
IDX_SCORES_TOP = 3
class A(gcj.base.GcjBase):

    def solve(self):
        print self.q
        i = 1
        for q in self.q:
            if self.isWin(q,'X') == True:
                text = "Case #" + str(i) + ": X won"
            elif self.isWin(q,'O') == True:
                text = "Case #" + str(i) + ": O won"
            elif q.find('.') != -1:
                text = "Case #" + str(i) + ": Game has not completed"
            else:
                text = "Case #" + str(i) + ": Draw"
            self.out_lines.append(text)
            i += 1

        
    def readInFile(self):
        gcj.base.GcjBase.readInFile(self)
        self.line_num = int(self.in_lines[0])
        del self.in_lines[0];
        self.q = ['']
        qi = 0
        for i in self.in_lines:
            if i  == '':
                print i
                self.q.append('')
                qi += 1
                continue
            self.q[qi] += i
        del self.q[qi] 
        return
    
    def isWin(self,data,sb):
        if data == '':
            return False
        #g = gcj.grid.Grid()
        #g.makeGrid(4,4)
        #g.fillGrid(data)
        #g.showGrid()
        data = data.replace('T', sb)
        print data
        winline = sb + sb + sb + sb
        # row
        s = [0,4,8,12]
        for i in s:
            print i
            line = data[i] + data[i+1] + data[i+2] + data[i+3]
            if line == winline:
                return True
        # column
        s = [0,1,2,3]
        for i in s:
            line = data[i] + data[i+4] + data[i+8] + data[i+12]
            if line == winline:
                return True

        # diagonal
        if (data[0] + data[5] + data[10] + data[15] == winline) or (data[3] + data[6] + data[9] + data[12] == winline):
            return True
        return
        


a = A()
#b.mizumashi(1000)
a.execute()
