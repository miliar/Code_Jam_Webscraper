#python 2.7

import sys
import math

def solve(D, P):
    Pindexed = zip([int(x) for x in P], range(len(P)))
    print [ x[0] for x in Pindexed ]
    print "\n"
    best = max(P)
    orig_best = best
    special_mins_best = 0
    special_mins = 0
    while True:
        new_max, index = max(Pindexed)
        print "Old best: " + str(best) + " candidate: " + str(new_max) + " " + str(special_mins)
        if (new_max + special_mins < best):
            best = new_max + special_mins
            special_mins_best = special_mins
        
        if special_mins > best:
            break
        if (new_max < 4):
            break
        rm_cakes = new_max/2
        if (new_max == 9):
            tmpP = Pindexed
            tmpP[index] = tuple([ 0, index ])
            tmp_max, tmp_index  = max(tmpP)
            print tmp_max
            if ((not tmp_max == 9) and (special_mins == 0)):

                alt, spec = solve(D, [ x[0] for x in tmpP ])
                if (alt - spec) <= 3:
                    rm_cakes = new_max/3
        #print "Temp max: " + str(tmp_max) + " of " + str([ x[0] for x in tmpP ])
        #if (new_max >= 9 and tmp_max <= new_max/3):
        #    rm_cakes = new_max/3
        #else:
 
        Pindexed[index] = tuple([ new_max - rm_cakes, index ])
        Pindexed.append(tuple([ rm_cakes, len(Pindexed) ]))
        special_mins += 1
        print [ x[0] for x in Pindexed ]
    print "Best: " + str(best) + " orig: " + str(orig_best) + " sm:" + str(special_mins)
    return int(best), special_mins_best

def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        print "Case #" + str(i + 1) 
        res = str(solve(int(split_input[1 + 2*i]), split_input[2 + 2*i].split(" "))[0])
        output_file.write("Case #" + str(i + 1) + ": " + res + "\n")
        print "\n\n\n"
    
if __name__ == "__main__":
    main()
