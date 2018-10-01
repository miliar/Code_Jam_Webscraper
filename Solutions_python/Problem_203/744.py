from sys import stdin, stdout

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.rowNum, self.colNum = (int(_) for _ in stdin.readline().split())
        self.grid = []
        for i in range(self.rowNum) :
            self.grid.append(list(stdin.readline()))

    def calculate(self) :
        self.seeds = []
        for row in range(self.rowNum) :
            for col in range(self.colNum) :
                if self.grid[row][col] != '?' :
                    self.seeds.append((row, col))

        for row, col in self.seeds :
            self.fill(row, col)
    
    def fill(self, row, col) :
        top = row - 1
        while top >= 0 and self.grid[top][col] == '?' :
            self.grid[top][col] = self.grid[row][col]
            top -= 1
        btm = row + 1
        while btm < self.rowNum and self.grid[btm][col] == '?' :
            self.grid[btm][col] = self.grid[row][col]
            btm += 1

        left = col - 1
        while left >= 0 :
            isOK = True
            for i in range(top + 1, btm) :
                if self.grid[i][left] != '?' :
                    isOK = False
                    break
            if isOK :
                for i in range(top + 1, btm) :
                    self.grid[i][left] = self.grid[row][col]
                left -= 1
            else :
                break

        right = col + 1 
        while right < self.colNum :
            isOK = True
            for i in range(top + 1, btm) :
                if self.grid[i][right] != '?' :
                    isOK = False
                    break
            if isOK :
                for i in range(top + 1, btm) :
                    self.grid[i][right] = self.grid[row][col]
                right +=1
            else :
                break

    def output(self, caseIndex) :
        stdout.write("Case #%d:\n" % caseIndex)
        for row in range(self.rowNum) :
            for col in range(self.colNum) :
                stdout.write("%s" % self.grid[row][col])
            stdout.write("\n")

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)

