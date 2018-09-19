INPUT = 'B-large.in'
OUTPUT = 'B-large.out'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class Basins:

    def __init__(self, infile = INPUT, outfile = OUTPUT):
        self.input = open(infile)
        self.output = open(outfile, 'w')
        
    def readElevations(self,H,W):

        elevations = []
        basins = []
        for h in range(H):
            row = [int(i) for i in self.input.readline().strip().split()]
            elevations.append(row)
            basins.append([0]*len(row))
        return elevations, basins
            
    def getDrainageDirection(self, i,j):
        # directions:
        # 0:sink, 1:north, 2:west, 3:east, 4:south
        
        if self.elevations[i][j] == 0: return 0
        minElev = self.elevations[i][j]
        direction = 0
        if i != 0 and self.elevations[i-1][j] < minElev:
            direction = 1
            minElev = self.elevations[i-1][j]
        if j != 0 and self.elevations[i][j-1] < minElev:
            direction = 2
            minElev = self.elevations[i][j-1]
        if j != len(self.elevations[0])-1 and self.elevations[i][j+1] < minElev:
            direction = 3
            minElev = self.elevations[i][j+1]
        if i != len(self.elevations)-1 and self.elevations[i+1][j] < minElev:
            direction = 4
        return direction

    def getBasin(self, i,j):
        d = self.getDrainageDirection(i,j)
        if d == 0:
            if not self.basins[i][j]:
                self.basins[i][j] = ALPHABET[self.numBasins]
                self.numBasins += 1
            return self.basins[i][j]
        elif d ==1:
            return self.getBasin(i-1,j)
        elif d ==2:
            return self.getBasin(i,j-1)
        elif d ==3:
            return self.getBasin(i,j+1)
        elif d ==4:
            return self.getBasin(i+1,j)

    def generateBasins(self):
        
        T = int(self.input.readline().strip())
        for t in range(T):

            self.numBasins = 0
            H,W = [int(i) for i in self.input.readline().strip().split()]
            self.elevations, self.basins = self.readElevations(H,W)
            #directions = generateDirectionMatrix(elevations)
            for i in range(H):
                for j in range(W):
                    b = self.getBasin(i,j)

                    if not b:
                        basins[i][j] = ALPHABET[self.numBasins]
                        self.numBasins += 1
                    else:
                        self.basins[i][j] = b
            self.output.write('Case #%d:\n' % (t+1))
            for i in range(len(self.basins)):
                self.output.write(' '.join(self.basins[i])+'\n')
##                print ' '.join(self.basins[i])
        self.output.close()
        self.input.close()


basins = Basins()
basins.generateBasins()
