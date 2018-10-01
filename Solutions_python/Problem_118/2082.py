#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      TrungDL
#
# Created:     13/04/2013
# Copyright:   (c) TrungDL 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    with open('C-small-attempt1.in') as f:
    #with open('test.in') as f:
        T = int(f.readline())
        for i in range(0, T):
            count = 0
            line = f.readline().strip().split(" ")
            minN = int(line[0])
            maxN = int(line[1])
            for num in range(minN, maxN+1):
                strnum = str(num)
                if(strnum == strnum[::-1]):
                    temp = int(math.floor(math.sqrt(num)))
                    if(temp*temp == num):
                        if(str(temp) == str(temp)[::-1]):
                            count = count+1
            print "Case #"+str(i+1)+": "+str(count)



if __name__ == '__main__':
    main()
