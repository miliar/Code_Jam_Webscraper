'''
Created on 2009. 8. 15.

@author: Bang, Hyunsu
'''

def process(data):
    letters = dict()
    mindata = list()
    count = 1;
    for letter in data:
        if not letter in letters:
            letters[letter] = count
            count = nextCount(count)
    for letter in data:
        mindata.append(letters[letter])
    base = len(letters)
    if base == 1:
        base = 2
    length = len(mindata)
    sum = 0
    print mindata
    for digit in mindata:
        length -= 1
        sum += digit * base ** length
    print sum
    return sum

def nextCount(num):
    if num == 1:
        return 0
    elif num == 0:
        return 2
    else:
        return num + 1

def main(input_fn):
    try:
        f = open(input_fn, 'r')
        o = open(input_fn+'.out', 'w')
    except IOError:
        print "Input file %s dos not exists" % (input_fn, )
        return 2
    
    lines = int(f.readline())
    for i in range(lines):
#        print process(f.readline().strip())
        res = str(process(f.readline().strip()))
        o.write('Case #' + str(i+1) + ': ' + res +'\n')
    
import sys
if __name__ == '__main__':
    main(sys.argv[1])