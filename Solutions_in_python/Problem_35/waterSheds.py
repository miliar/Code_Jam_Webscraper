
class run():
    def __init__(self, file):
        maps = int(file.readline())
        self.output = ''
        for case in range(maps):
            line = file.readline()
            [self.H, self.W] = [int(i) for i in line.split(" ")]

            self.map = []
            for row in range(self.H):
                line = file.readline()
                self.map.append([int(i) for i in line.split(" ")])
            self.regions = []
            for y in range(self.H):
                self.regions.append([])
                for x in range(self.W):
                    self.regions[-1].append({'H': self.map[y][x], 'down': [], 'basin': 0, 'label': ''})
                    
            self.flow()

            self.output += "Case #%s:\n" %(case + 1)
            self.output += self.labelMap()

            

            
    def dispMap(self):
        line = ''
        for y in self.map:
            for x in y:
                line += str(x) + " "
            line += '\n'
        print line

    def labelMap(self):
        output = ""
        for y in self.regions:
            for x in y:
                output += str(x['label']) + ' '
            output += "\n"
        return output
            

    def reverse(self,direction):
        l = {'south': 'north', 'north': 'south', 'east': 'west', 'west': 'east'}
        return l[direction]
    
    def flow(self):

        
        order = self.getOrder()
        
        for each in order:
            data = self.inFlow(each)
            
            self.regions[each[0]][each[1]]['coords'] = each
            self.regions[each[0]][each[1]]['up'] = data

            for i in data:
                lower = self.getClose(each[::], i)
                self.regions[lower[0]][lower[1]]['down'].append(self.reverse(i))

        basin = 1
        
        for each in order:
            if self.regions[each[0]][each[1]]['basin'] == 0: 
                self.recursive(each[::], basin)
                basin += 1

        convTable = [''] * 27
        label = 'a'

        for y in self.regions:
            for x in y:
                if convTable[x['basin']] == '':
                    convTable[x['basin']] = label
                    label = chr(ord(label) + 1)
                x['label'] = convTable[x['basin']]

        


    def recursive(self,coords, basin):
        self.regions[coords[0]][coords[1]]['basin'] = basin
        connected = self.regions[coords[0]][coords[1]]['up']
        for direction in connected:
            next = self.getClose(coords[::], direction)
            if self.regions[next[0]][next[1]]['basin'] == 0:
                self.recursive(next[::], basin)
                
    


    def getClose(self, coords, direction):
        if direction == 'south':
            coords[0] += 1
        elif direction == 'north':
            coords[0] -= 1
        elif direction == 'east':
            coords[1] += 1
        elif direction == 'west':
            coords[1] -= 1
            
        if coords[0] >= 0 and coords[0] < self.H and coords[1] >= 0 and coords[1] < self.W:
            return coords[::]
        else:
            return 'x'

    def inFlow(self, coords):
        # returns the direction of water flowing in
        # for the four adjecent sides.


        adjecent = {'north': self.getClose(coords[::], 'north'),
                    'east' : self.getClose(coords[::], 'east'),
                    'south': self.getClose(coords[::], 'south'),
                    'west' : self.getClose(coords[::], 'west')}


        inFlows = []

        for side in adjecent:
            if adjecent[side] != 'x':
                if self.outFlow(adjecent[side]) == self.reverse(side):
                    inFlows.append(side)

        return inFlows
            
        
                
    def outFlow(self, coords):
        #returns the direction of water flowing out

        height = self.getPoint(coords)
        
        next = {}
        next['south'] = self.getPoint([coords[0]+1, coords[1]])
        next['west']  = self.getPoint([coords[0], coords[1]-1])
        next['north'] = self.getPoint([coords[0]-1, coords[1]])
        next['east']  = self.getPoint([coords[0], coords[1]+1])


        smallest = 'north'
        for dir in next:
            if next[dir] != 'x':
                if next[smallest] == 'x':
                    smallest = dir
                if next[dir] < next[smallest]:
                    smallest = dir

        if self.getPoint(coords) <= next[smallest]:
            smallest = ''

               
        return smallest

    def getOrder(self):
        line = []
        for i in self.map:
            line += i
        lineS = line[::]
        lineS.sort() # sort lineS 
        order = []
        old = lineS[0]
        here = 0
        for i in lineS:
            if i == old:
                next = line.index(i, here)
                here = next + 1
                order.append(next)
            else:
                next = line.index(i)
                here = next + 1
                order.append(next)
                old = i
                
        coordOrder = []
        for i in order:
            coordOrder.append([i/self.W, i % self.W])

        return coordOrder
        

    def getPoint(self, coords):
        if coords[0] < 0:
            return 'x'
        else:
            if coords[1] < 0:
                return 'x'
            else:
                try: return self.map[coords[0]][coords[1]]
                except: return 'x'
        
            

file = open("B-large.in")
result = run(file)
file.close()
file = open("B-large.out", 'w')
file.write(result.output)
file.close()
