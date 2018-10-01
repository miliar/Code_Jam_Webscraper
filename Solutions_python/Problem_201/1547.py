from math import log, floor, ceil, pow

def find_level(n):
    return floor(log(n, 2)) 

def num_in_prev(level):
    return max(pow(2, level) - 1, 0)

def interval_size_level(level, total_stalls):
    prev = num_in_prev(level)
    return floor((total_stalls - prev) / (prev+1))

def num_plus_one(level, num_people, total_stalls):
    prev = num_in_prev(level)
    return (total_stalls - prev) % (prev+1)
    
def number_in_level(level, k):
    return k - num_in_prev(level)

def solve(n, k):
    #print "input"
    #print n, k
    level = find_level(k)
    #print "level"
    #print level
    #print "num in prev"
    #print num_in_prev(level)
    size = interval_size_level(level, n)
    #print "Size %d" % size
    #print num_plus_one(level, k, n)
    if number_in_level(level, k) <= num_plus_one(level, k, n):
        size += 1
    return int(ceil((size - 1)/2)), int(floor((size - 1)/2))


def solve_for_file(file_loc, o_loc):
    count = 1
    with open(file_loc, "r") as f:
        with open(o_loc, "w") as o:
            for line in f:
                split_up = line.split(" ")
                if len(split_up) == 2:
                    o.write("Case #%d: " % count)
                    res = solve(int(split_up[0]), int(split_up[1]))
                    o.write("%d %d" % (res[0], res[1]))
                    o.write("\n")
                    print res                    
                    count += 1

solve_for_file("small_two_dat.txt", "small_two_out.txt")
    
