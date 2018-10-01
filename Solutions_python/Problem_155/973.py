'''
Created on Apr 11, 2015

@author: lroot
'''
from __future__ import print_function



if __name__ == '__main__':
    input_fname = "../q1.txt"
    output_fname = "../a1.txt"
    content = []
    with open(input_fname) as inf:
        content = inf.readlines()
    outf = open(output_fname, 'w')
    
    i = 0  
    for idx, line in enumerate(content):
        if idx == 0:
            continue
        else:
            data = line.split(" ")
            nums = [int(num) for num in (data[1].strip())]
            sum_audience = 0
            index = 0
            new_audience = 0
            for num in (nums):
#                 print num
#                 print str(index) + " "+ str(num) +" "+str(sum_audience)
                audience = sum_audience - index
#                 print audience
                if audience < 0 :
                    new_audience = new_audience + abs(audience)
                    sum_audience = sum_audience + abs(audience)
                sum_audience = sum_audience + num
                index = index + 1
           # Case #1: 0
            outf.write("Case #"+str(idx)+": " + str(new_audience)+'\n')
            
#                 print idx