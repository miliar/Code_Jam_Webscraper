#-------------------------------------------------------------------------------
# Name:        Recycled Numbers
# Purpose:
#
# Author:      udonko
#
# Created:     14/04/2012
# Copyright:   (c) udonko 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
def main():
    input = open("input.txt","r")
    output = open("output.txt","w")
    try:
        temp = input.readline()
        t = int(temp)
        for i in range(t):
            #sys.stdout.write("-------\n")
            temp = input.readline()
            temp = temp.strip()
            temps = temp.split()
            a = int(temps[0])
            b = int(temps[1])



            result = calc(a,b, temps[0],temps[1])
            outtext ="Case #"+str(i+1)+": "+str(result)+'\n'
            output.write(outtext)
            sys.stdout.write(outtext)
    finally:
        input.close()
        output.close()
def calc(a,b, txta, txtb):
    if a<10:
        return 0
    if a==b:
        return 0
    numofdegits = len(txta)

    count = 0

    for temp in openNumIterator(a, b):
        n = int(temp)
#        sys.stdout.write("===="+temp+'\n')
        for i in range(1,numofdegits):
            numstr = temp[i:]+temp[:i]

            m = int(numstr)
            if a<=n<m<=b:
                count+=1
                sys.stdout.write('('+temp+','+numstr+'):'+str(count)+'\n')

    return count

def openNumIterator(a,b):

    for n in range(a,b+1):
        if a<=n<=b:
            yield str(n)
        else:
            continue

if __name__ == '__main__':
    main()
