'''
Created on Apr 13, 2013

@author: hou
'''

import sys, math


def ispalindrome(word):
    word = str(word)
    return word == word[::-1]


def get_fair_num(start, end):
    start = int(math.ceil(math.sqrt(start)))
    end = int(math.sqrt(end))
    num = 0
    
    for i in xrange(start, end+1):
        if ispalindrome(i) and ispalindrome(i*i):
            num += 1
    
    return num


def main():    

    infile = open(sys.argv[1])          # input file as the first arg
    outfile = open(sys.argv[2], 'w')    # output file as the second arg
    
    # get the number of test cases
    test_num = int(infile.readline())
        
    # for each test case, determine the status
    for i in xrange(test_num):
        [start, end] = [int(elem) for elem in infile.readline().split()]
        result = get_fair_num(start, end)
        outfile.write("Case #" + str(i+1) + ": " + str(result) + '\n')
    
    # close files
    infile.close()
    outfile.close()  



if __name__ == '__main__':
    main()

