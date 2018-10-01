#! /usr/bin/python
import sys

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

def count(line,k,turn):
    return int(line[k][0:2])*60 + int(line[k][3:5]) + turn

# todo: binary search
def find(list,mem,len):
    for i in range(len):
        if list[i] > mem:
            return i
    return -1

while actual_case < cases:
    actual_case += 1
    turn = int(sys.stdin.readline()[:-1])
    
    numbers = sys.stdin.readline()[:-1].split()
    na = int(numbers[0])
    nb = int(numbers[1])
    
    list_na = []
    list_nb = []
    
    for i in range(na):
        line = sys.stdin.readline()[:-1].split()
        l0 = count(line,0,0)
        l1 = count(line,1,turn)
        list_na.append((l0,l1))
     
    for i in range(nb):
        line = sys.stdin.readline()[:-1].split()
        l0 = count(line,0,0)
        l1 = count(line,1,turn)
        list_nb.append((l0,l1))
    
    list_na.sort()
    list_nb.sort()

    list = [[]]
    list = [list_na,list_nb]

    length = [na,nb]
    result = [0,0]

    while list[0] or list[1]:
        if list[0] and list[1]:
            if list[0][0] > list[1][0]:
                which = 1 
                result[1] += 1
            else:
                which = 0 
                result[0] += 1
            index = 0
            while index > -1:
                begin,end = list[which].pop(index)
                length[which] -= 1
                which = (which + 1) % 2 
                index = find(list[which],(end,0),length[which])
        elif list[0]:
            result[0] += len(list[0])
            break
        elif list[1]:
            result[1] += len(list[1])
            break

    print "Case #%d: %d %d" %(actual_case,result[0],result[1])
