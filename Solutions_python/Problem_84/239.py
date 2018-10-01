import sys

def fillRed(picture, x, y):
    # Check Bound First
    if x + 1 >= C:
        return -2
    if y + 1 >= R:
        return -3

    # Check 4 tile are all "#"
    if picture[y][x] == "#" and picture[y+1][x] == "#" and picture[y][x+1] == "#" and picture[y+1][x+1] == "#":
        picture[y][x] = "/"
        picture[y][x+1] = "\\"
        picture[y+1][x] = "\\"
        picture[y+1][x+1] = "/"
        return 0
    return -1
def replaceRed(picture):
    for y in range(R - 1):
        for x in range(C - 1):
            if picture[y][x] == "#":
                ret = fillRed(picture, x, y)
                if ret == 0:
                    pass
                else:
                    #print x,y
                    return ret # Fail
    #check last row and column
    for y in range(R):
        if picture[y][-1] == "#":
            return -1
    for x in range(C):
        if picture[-1][x] == "#":
            return -1
        
    return 0 # Success
def PrintPicture(picture):
    for d in picture:
        print "".join(d)
if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(sys.argv[1], "r")
        T = int(f.readline().strip())
        for _t in range(T):
            picture = []
            R, C = map(int, f.readline().strip().split())
            for _r in range(R):
                picture.append(list(f.readline().strip()))

            #print picture
            ret = replaceRed(picture)
            
            print "Case #%d:" %(_t + 1)
            if ret == 0:
                PrintPicture(picture)
            else:
                print "Impossible"
        f.close()
