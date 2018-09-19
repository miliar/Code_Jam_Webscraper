#!/usr/bin/python

import sys
import math

def isBigger(list1, list2):
    for i in range(len(list1)):
        if list1[len(list1)-1-i] > list2[i]:
            #print 'bigger'
            return 1
        elif list1[len(list1)-1-i] < list2[i]:
            #print 'smaller'
            return 0
    #print 'equal'
    return 0

def isEven(list):
    if (len(list)-1)%2 == 0:
        return 1
    else:
        return 0

def copy(list):
    if isEven(list):
        list1 =  list[:len(list)/2]
        if isBigger(list1, list[len(list)/2:-1]):
            list[len(list)/2:]=reversed(list1)
        elif list1[len(list1)-1] != '9':
            list[len(list)/2-1] = list1[len(list1)-1] = str(int(list1[len(list1)-1])+1)
            list[len(list)/2:]=reversed(list1)
        else:
            for i in range(len(list1)):
                if list1[len(list1)-1-i] == '9':
                    list1[len(list1)-1-i] = '0'
                else:
                    list1[len(list1)-1-i] = str(int(list1[len(list1)-1-i])+1)
                    break
            if list1[0] == '0':
                list1.insert(0,'1')
                list[:len(list)/2] = list1
                list[len(list)/2-1:] = reversed(list1)
            else:
                list[:len(list)/2] = list1
                list[len(list)/2:] = reversed(list1)
    else:
        list1 = list[:len(list)/2-1]
        if isBigger(list1, list[len(list)/2:-1]):            
            list[len(list)/2:]=reversed(list1)
        elif list[len(list)/2-1] != '9':
            list[len(list)/2-1] = str(int(list[len(list)/2-1])+1)
            list[len(list)/2:]=reversed(list1)
        else:
            list[len(list)/2-1] = '0'
            for i in range(len(list1)):
                if list1[len(list1)-1-i] == '9':
                    list1[len(list1)-1-i] = '0'
                else:
                    list1[len(list1)-1-i] = str(int(list1[len(list1)-1-i])+1)
                    break

            if list1[0] == '0':
                list1.insert(0,'1')
                list[:len(list)/2-1] = list1
                list[len(list)/2:] = reversed(list1)
            else:
                list[:len(list)/2-1] = list1
                list[len(list)/2:] = reversed(list1)
    return list

def nextPalindrome(list):
    result = []
    if len(list) == 2:
        if list[0] != '9':
            return int(list[0])+1
        else:
            return '11'
    result = ",".join( copy(list))
    result = result.replace(",",'')
    return result 

def isPalindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False

def main():
    fd = open('C-large-1.in','r')
    fw = open('output.txt','w')
    line = fd.readline()
    num_cases = int(line)
    
    
    fairAndSquare = []
    i = 0
    while (i**2 < 10**15):
        l = list(str(i)+"\n")
        i = int(nextPalindrome(l))
        if isPalindrome(i):
            if isPalindrome(i**2):
               fairAndSquare.append(i**2)
               
    for i in range(num_cases):   
        count = 0
        pair = fd.readline().split()
        small = int(pair[0])
        large = int(pair[1])
        l = list(str(small-1)+'\n')
        
        
        for num in fairAndSquare:
            if num>=small and num<=large:
                count = count +1
        
        #small = int(nextPalindrome(l))
        #while small <= large:
            #root = math.sqrt(small)
            #if (root-int(root)) == 0:
                #if isPalindrome(int(root)):
                    #count = count +1
            #l = list(str(small)+'\n')
            #small = int(nextPalindrome(l))
            #print small
        fw.write('Case #'+str(i+1)+': '+str(count)+'\n')
        
        

        
    
    
#    for i in range(num_terms):
#        line = sys.stdin.readline()
#        l = list(line)
#        print nextPalindrome(l)

if __name__=='__main__':
    main()