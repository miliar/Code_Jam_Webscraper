# lawnmower.py
#
# For Google Code Jam 2013
# David Lister
#

class Lawn:

    def __init__(self, lst):
        self.width = int(lst[0][1])
        self.height = int(lst[0][0])
        self.lawn = lst[1:]
        for x in range(self.height):
            for y in range(self.width):
                self.lawn[x][y] = int(self.lawn[x][y])

        
        self.lawn_rotated = []
        for col in range(self.width):
            line = []
            for row in range(self.height):
                line.append(self.lawn[row][col])
            self.lawn_rotated.append(line)
            

    def test_horizontal(self, row, col):
        if self.lawn[row][col] == max(self.lawn[row]):
            return True
        return False

    def test_vertical(self, row, col):
        if self.lawn[row][col] == max(self.lawn_rotated[col]):
            return True
        return False

    def test(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.test_vertical(row, col) or self.test_horizontal(row, col):
                    pass
                
                else:
                    return False
        return True


   
fname = raw_input('Please enter file name: ')
fout = str(fname.split('.')[0]) + '.txt'

f = list(open(fname, 'r'))

lawns = []
lawn = []
lawns_left = int(f[0][:-1])
lawn_lines = 0
i = 1

over = False
while not over:
    try:
        if lawn_lines == 0:
            lawn_lines = int(f[i].split(' ')[0]) + 1
            lawns.append(lawn)
            lawn = []

        lawn.append(f[i][:-1].split(' '))
            
        

        i += 1
        lawn_lines -= 1
    except:
        over = True
        
lawns.append(lawn)
lawns = lawns[1:]

del lawn

lawn_list = []
for lawn in lawns:
##    for line in lawn:
##        print line
##    print
    lawn_list.append(Lawn(lawn))


output = ''
for i in range(len(lawn_list)):
    if lawn_list[i].test():
        output = output + 'Case #' + str(i + 1) + ': YES\n'
        
    else:
        output = output + 'Case #' + str(i + 1) + ': NO\n'


out = open(fout, 'w')
out.write(output)
out.close()

print output


