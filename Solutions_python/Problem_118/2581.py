import os
import sys
import math



def count_pali_square_pali_in_range(start, end):
    root_space_start = int(math.ceil(math.sqrt(start)))
    root_space_end = int(math.floor(math.sqrt(end)))
    root_space_square = (root_space_start) * (root_space_start);
    pali_square_count = 0;
    for i in xrange(root_space_start, root_space_end+1):
        if str(i) == str(i)[::-1]:
            if str(root_space_square) == str(root_space_square)[::-1]:
                ###This is counted
                pali_square_count += 1;
        root_space_square = root_space_square + 1 + 2*i;
    return pali_square_count;
           

def count_paplidromes(in_file):
    fi = open(in_file, "r");
    test_case_count = int(fi.readline());
    for test_case_num in xrange(1, test_case_count+1):
        global_count = 0;
        (start, end) = fi.readline().strip().split();
        start = int(start);
        end = int(end);
        global_count += count_pali_square_pali_in_range(start, end);
        print "Case #%d: %d"%(test_case_num, global_count);


count_paplidromes(sys.argv[1]);
