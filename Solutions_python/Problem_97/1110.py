import sys
import re

def is_bad(i):
    str_i = str(i)
    lst1 = [ch for ch in str_i]
    return lst1

def match(a,  b):
    res = 0
    old_res = 0;
    for i in range(a, b, 1):
        lst1 = is_bad(i)
        if len(lst1) == 0:
            continue
        for j in range(i+1, b+1, 1):
            lst2 = is_bad(j)
            if len(lst2) == 0:
                continue
            if (len(lst1) < 2) or (len(lst2) < 2) or (len(lst1) !=len(lst2)):
                continue
            for k in range(len(lst1)-1):
                lst2.insert(0,  lst2.pop())
                if (lst2[0] == 0):
                    continue
                if lst1 == lst2:
                    res+=1
                    break
    return res


if len(sys.argv) < 3:
    raise Exception('error arg',  'file name not found')
fr=None
fw=None
try:
    fr = open(sys.argv[1], 'r')
    fw = open(sys.argv[2], 'w')
    T = int(re.split('\D+',  fr.readline())[0])
    i = 1
    while (T>=i):
        numbers = re.split('\D+',  fr.readline())
        a = int(numbers[0])
        b = int(numbers[1])
        res = match(a, b)
        newline ='Case #{0}: {1}\n'.format(i, res)
        fw.write(newline)
        i=i+1
finally:
    if fr!=None:
        fr.close()
    if fw!=None:
        fw.close()
