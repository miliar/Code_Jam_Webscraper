
__author__="eugen"
__date__ ="$Sep 3, 2009 10:53:59 AM$"


def solve(hmap, h, w, basin_labels):
    labelmap = {}
    for i in range(0,h):
        for j in range(0,w):
          coordinate = j,i
          if coordinate not in labelmap:
            #coordinate not yet labeled track its flow
            currx, curry = coordinate
            common_basin = set([coordinate])
            sink_found = False

            while sink_found == False:
                dest = find_dest((currx,curry), hmap, h, w)

                #if there is no destination, we have a sink
                if dest == (-1,-1):
                    sink_found = True
                else:
                    # add dest to common basin
                    if dest in labelmap:
                        sink_found = True
                    currx,curry = dest
                    common_basin.add(dest)

            #sink is found, check its label
            if dest in labelmap:
                label = labelmap[dest]
            else:
                label = basin_labels[0]
                basin_labels = basin_labels[1:]
            for coord in common_basin:
                    labelmap[coord] = label
    return labelmap

def find_dest(coordinate, hmap, h, w):
            x,y = coordinate
            dest = -1,-1
            hmap[dest] = -1
            #check north
            if ((y > 0)):
                if( (hmap[coordinate] > hmap[x,y-1])):
                    dest = x,(y-1)
            #check west
            if ((x > 0)):
                if( (hmap[coordinate] > hmap[x-1,y]) & ((dest == (-1,-1)) | (hmap[x-1,y] < hmap[dest])) ):
                    dest = x-1,y
            #check east
            if (x < (w-1)):
                if( (hmap[coordinate] > hmap[x+1,y]) & ((dest == (-1,-1)) | (hmap[x+1,y] < hmap[dest])) ):
                    dest = x+1,y
            #check south
            if (y < (h-1)):
                if( (hmap[coordinate] > hmap[x,y+1]) & ((dest == (-1,-1)) | (hmap[x,y+1] < hmap[dest]))):
                    dest = x,(y+1)
            #print "dest of {0} is {1}".format(coordinate, dest)
            return dest

if __name__ == "__main__":
    with open("B-small-attempt0.in") as f:
        lines = f.readlines()
        head = lines.pop(0)
        cases = int(head)
        for case in range(1,cases+1):
            print "Case #{0}:".format(case)
            heightmap = {}
            dim = lines.pop(0).split()
            h, w = int(dim[0]), int(dim[1])
            # build heightmap
            for row in range(0, h):
                heights = lines.pop(0)[:-1].split()
                for col in range(0, w):
                    heightmap[(col,row)] = heights[col]
            #print heightmap
            labels = solve(heightmap, h , w, "abcdefghijklmnopqrstuvwxyz")
            for row in range(0, h):
                for col in range(0, w):
                    print labels[col,row],
                print ""
            
    #print "Hello";