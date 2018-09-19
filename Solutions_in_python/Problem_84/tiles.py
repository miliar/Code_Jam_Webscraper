import sys
import time
from itertools import combinations


def possible_red(curr_pixels):

    maxx = -sys.maxint
    maxy = -sys.maxint
    minx = sys.maxint
    miny = sys.maxint

    for pixel in curr_pixels:
        maxx = max(maxx, pixel[0])
        minx = min(minx, pixel[0])
        maxy = max(maxy, pixel[1])
        miny = min(miny, pixel[1])

    if not abs(maxy-miny) == 1:
        return False
    if not abs(maxx-minx) == 1:
        return False

    return True


def further(all_pixels, order):

    if not all_pixels:
        return True, order

    combs = combinations(all_pixels, 4)
    for comb in combs:
        if not possible_red(comb):
            continue
        curr_pixels = all_pixels[:]
        for pixel in comb:
            curr_pixels.remove(pixel)

        return further(curr_pixels, order + comb)
    return False, order


def corner(pixel, minx, maxx, miny, maxy):

    if pixel[0] == miny and pixel[1] == minx:
        return '/'
    elif pixel[0] == maxy and pixel[1] == maxx:
        return '/'
    else:
        return '\\'

if __name__ == "__main__":

    t1 = time.clock()

    f = open(sys.argv[1])
    testcount = int(f.readline())

    for testindex in range(0, testcount):

        line = f.readline()
        vals = line.strip().split()

        r = int(vals[0])
        c = int(vals[1])

        image = []
        bluepixels = []
        for row in range(0,r):
            line = f.readline()
            pixels = list(line.strip())
            image.append(pixels)
            for column,pixel in enumerate(pixels):
                if pixel == '#':
                    bluepixels.append((row, column))


        combs = combinations(bluepixels, 4)
        possible = False
        for comb in combs:
            all_pixels = bluepixels[:]

            if not possible_red(comb):
                continue

            for pixel in comb:
                all_pixels.remove(pixel)

            val, order = further(all_pixels, comb)
            if not val:
                continue
            else:
                possible = True
                break

        print "Case #%i:" % (testindex+1)
        if not possible:
            if bluepixels:
                print "Impossible"
            else:
                for i in range(0, r):
                    for j in range(0, c):
                        sys.stdout.write(image[i][j])
                    sys.stdout.write("\n")
        else:
            for red in range(0, len(bluepixels)/4):

                first = order[red*4]
                second = order[red*4+1]
                third = order[red*4+2]
                fourth = order[red*4+3]

                max_y = max(first[0], second[0], third[0], fourth[0])
                min_y = min(first[0], second[0], third[0], fourth[0])
                max_x = max(first[1], second[1], third[1], fourth[1])
                min_x = min(first[1], second[1], third[1], fourth[1])

                image[first[0]][first[1]] = corner(first, min_x, max_x, min_y, max_y)
                image[second[0]][second[1]] = corner(second, min_x, max_x, min_y, max_y)
                image[third[0]][third[1]] = corner(third, min_x, max_x, min_y, max_y)
                image[fourth[0]][fourth[1]] = corner(fourth, min_x, max_x, min_y, max_y)

            for i in range(0, r):
                for j in range(0, c):
                    sys.stdout.write(image[i][j])
                sys.stdout.write("\n")



    t2 = time.clock()
    sys.stderr.write("runtime: %s\n" % repr(t2-t1))
