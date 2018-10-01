#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nishant
#
# Created:     12-04-2014
# Copyright:   (c) Nishant 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    input_file  = "E:\Dropbox\CodeBase\Python\GoogleCodeJam_2014\A-small-attempt0.in"
    output_file = "E:\Dropbox\CodeBase\Python\GoogleCodeJam_2014\A-output.txt"
    f = open(input_file, 'r')
    o = open(output_file, 'w')

    cases = int(f.readline())
    lst = list(f)

    i = 0
    j = 1
    while i < (cases * 10):
        first = int(lst[i])
        # print (first)
        arr1 = [lst[i+1], lst[i+2], lst[i+3], lst[i+4]][first-1]
        # print (arr1)
        i += 5
        sec = int(lst[i])
        # print (sec)
        arr2 = [lst[i+1], lst[i+2], lst[i+3], lst[i+4]][sec-1]
        # print (arr2)
        i += 5

        set1 = set(arr1.split())
        set2 = set(arr2.split())
        # print (set1)
        # print (set2)

        res = set1 & set2

        if len(res) == 0:
            o.write ("Case #%s: Volunteer cheated!\n" %(j))
        elif len(res) > 1:
            o.write ("Case #%s: Bad magician!\n" %(j))
        else:
            o.write ("Case #%s: %s\n" %(j, next(iter(res))))
        j += 1

    f.close()
    o.close()



if __name__ == '__main__':
    main()