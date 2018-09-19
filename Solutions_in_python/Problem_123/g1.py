from itertools import count
big=0xFFF

def func(x, lst):
    lst.sort()
    for i, num in enumerate(lst):
        if num<x:
            x+=num
        else:
            break
    newlst=lst[i:]
    return min(findB(x, newlst, j) for j in range(len(newlst)+1))

def findA(x, lst):
    peulot=0
    for num in lst:
        c=0
        while(num>=x):
            peulot+=1
            x=2*x-1
            if peulot>big:
                return big
        x+=num
    return peulot

def findB(x, lst, j):
    if j==0:
        return findA(x, lst)
    return findA(x, lst[:-j])+j

def array(x):
    return (i*x+1-i for i in (pow(2, j) for j in count() ))

file=open(r"C:\Users\user\Downloads\A-large (1).in").read().splitlines()[1:]
i=1
while file:
    x=int(file[0].split(' ')[0])
    lst=list(map(int, file[1].split(' ')))
    print("Case #"+str(i)+":", func(x, lst))
    i+=1
    file=file[2:]
