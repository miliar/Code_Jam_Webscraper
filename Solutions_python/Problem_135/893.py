#!/usr/bin/env python
import sys

def print_result(tc_number, res):
    print "Case #{0}:".format(tc_number), res

def main():
    data = sys.stdin
    N = int(data.readline())
    
    test_case = 1       
    while test_case <= N:
        row1, row2 = [], []
        
        answer1 = int(data.readline())
        # print answer1
        for x in xrange(1, 5):
            if answer1 == x:
                row1 = map(int, data.readline().split())
            else:
                data.readline()
        #
        answer2 = int(data.readline().rstrip())
        for x in xrange(1, 5):
            if answer2 == x:
                row2 = map(int, data.readline().split())
            else:
                data.readline()        
        result = list(set(row1) & set(row2))
        len_result = len(result)
        if len_result == 1:
            print_result(test_case, result[0])
        elif len_result == 0:
            print_result(test_case, "Volunteer cheated!")
        else:
            print_result(test_case, "Bad magician!")

        test_case += 1    

    
if __name__ == '__main__':
    main()