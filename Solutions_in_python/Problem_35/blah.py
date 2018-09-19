import sys

def main(argv):
    ifilename = argv[1]
    ofilename = argv[2]
    ifile = open(ifilename, 'r')
    numlines = ifile.readline()
    ofile = open(ofilename, 'w')
    numlines = numlines.strip();
    num = int(numlines)
    labeler = Labeler()
    
    for i in range(num):
        dimensions = ifile.readline().strip().split(" ")
        H,W = int(dimensions[0]),int(dimensions[1])
        altitudes = []
        ofile.write("Case #"+str(i+1)+":\n")
        for y in range(H):
            a = ifile.readline().strip().split(" ")
            b = []
            for x in range(W):
                b.append(int(a[x]))
            altitudes.append(b)
                
        labels = labeler.generateLabels(altitudes, H, W)
        
        for y in range(H):
            for x in range(W):
                ofile.write(labels[y][x]+" ")
            ofile.write("\n")
    
    ifile.close()
    ofile.close()

class Labeler:
    
    sink = -1
    north = 0
    west = 1
    east = 2
    south = 3
    
    directions = []
    labels = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
        
    def generateLabels(self, altitudes, H, W):
        self.directions = [ [self.sink for x in range(W)] for y in range(H) ]
        for y in range(H):
            for x in range(W):
                least = altitudes[y][x]
                direction = self.sink
                if -1 < x < W and -1 < y-1 < H and altitudes[y-1][x] < least:
                    least = altitudes[y-1][x]
                    self.directions[y][x] = self.north
                if -1 < x-1 < W and -1 < y < H and altitudes[y][x-1] < least:
                    least = altitudes[y][x-1]
                    self.directions[y][x] = self.west
                if -1 < x+1 < W and -1 < y < H and altitudes[y][x+1] < least:
                    least = altitudes[y][x+1]
                    self.directions[y][x] = self.east
                if -1 < x < W and -1 < y+1 < H and altitudes[y+1][x] < least:
                    self.directions[y][x] = self.south
                    
        self.reallyGenerateLabels(H, W)
        return self.labels
    
    def reallyGenerateLabels(self, H, W):
        self.labels = [ ["" for x in range(W)] for y in range(H) ]
        #print self.directions
        self.nextlabel = 0
        for y in range(H):
            for x in range(W):
                #print "==============================="
                #print self.labels
                self.findLabel(x,y)
    
    def findLabel(self, x, y):
        #print "("+str(y)+","+str(x)+") - "
        if self.labels[y][x] != "":
            return
            #print "already set"
        elif self.directions[y][x] == self.sink:
            self.labels[y][x] = self.alphabet[self.nextlabel]
            #print "sink "+self.alphabet[self.nextlabel]
            self.nextlabel += 1
        elif self.directions[y][x] == self.north:
            #print "going north"
            if self.labels[y-1][x] == "":
                self.findLabel(x,y-1)
            self.labels[y][x] = self.labels[y-1][x]
        elif self.directions[y][x] == self.west:
            #print "going west"
            if self.labels[y][x-1] == "":
                self.findLabel(x-1,y)
            self.labels[y][x] = self.labels[y][x-1]
        elif self.directions[y][x] == self.east:
            #print "going east"
            if self.labels[y][x+1] == "":
                self.findLabel(x+1,y)
            self.labels[y][x] = self.labels[y][x+1]
        elif self.directions[y][x] == self.south:
            #print "going south"
            if self.labels[y+1][x] == "":
                self.findLabel(x,y+1)
            self.labels[y][x] = self.labels[y+1][x]

if __name__ == '__main__':
    main(sys.argv)