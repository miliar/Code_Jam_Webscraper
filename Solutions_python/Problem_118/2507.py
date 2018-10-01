import sys

import math
import bisect
import itertools

def debug(msg):
    #print msg
    pass
def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i == len(a):
        return i - 1
    elif a[i] == x:
            return i
    else:
        return i - 1
    raise ValueError


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError



def split_range(l, min, max):
    
    max_index = find_le(l, max)
    min_index = find_ge(l, min)

    return l[min_index : max_index + 1]
    


def find_root_range(min, max):
    root_min = int(math.ceil(math.sqrt(min)))
    root_max = int(math.floor(math.sqrt(max)))

    debug("root range %d %d -> %d %d" % (min, max, root_min, root_max))
    return (root_min, root_max)



def gen_pals_of_size(k):
    debug("gen pals %d" % k)
    if k == 1:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]

    return [int(''.join(map(str, (([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
            else ([x]+list(ys)+list(ys)[::-1]+[x])))))
            for x in range(1,10)
                for ys in itertools.permutations(range(10), k/2-1)
                    for z in (range(10) if k%2 else (None,))]

def gen_palindromes(min, max):
    
    str_min = str(min)
    str_max = str(max)

    for i in range(len(str_min), len(str_max) + 1):
        pals = gen_pals_of_size(i)
        pals = split_range(pals, min, max)
        for pal in pals:
            yield pal

def is_pal(str_num):
   
    if len(str_num) == 1:
         return True

    return str_num[0] == str_num[-1] and is_pal(str_num[1:-1])
    

def run(min, max):

    num_fair_squares = 0
    (min, max) = find_root_range(min, max)
    
    pal_gen = gen_palindromes(min, max)
    for root_pal in pal_gen:
        debug("root pal: %d" % root_pal)
        if is_pal(str(int(math.pow(root_pal, 2)))):
            num_fair_squares += 1
            debug("found pal %d" % root_pal)
    return num_fair_squares

def test_split():
    x = [1,2,3,4,5,6]
    y = split_range(x, 2,5)
    print "split 2,5 %s %s" % (str(x), str(y))
    x = [1,2,3,4,5,10]
    y = split_range(x,1,7)
    print "split 1,7 %s %s" %(str(x), str(y))
    x = [1,5,6,7,8]
    y = split_range(x,2,8)
    print "split 2,8 %s %s" %(str(x), str(y))

#fsqs = run(int(sys.argv[1]),int(sys.argv[2]))
#print fsqs

def runner(input_file):
    lines = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    index = 0
    num_tests = int(lines[index].strip())
    index += 1

    for test in range(num_tests):
        # skip empty lines
        while lines[index].strip() == "":
            index += 1
        
        (min, max) = lines[index].strip().split(" ")
        res = run(int(min), int(max))
        debug("case %d %s %s" % (test, min, max)) 
        print "Case #%d: %d" % (test + 1, res)
        index +=1


runner(sys.argv[1])


        
