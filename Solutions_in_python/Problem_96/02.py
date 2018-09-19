import sys
import re

def match(S,  p,  lst):
    res = 0
    for str_num in lst:
        num = int(str_num)
        if p<=(num/3):
            res+=1
            continue
        num -= p
        if num < 0:
            continue
        if (num+2) >= (p*2):
            res+=1
            continue
        if ((num+4) >= (p*2)) and (S > 0):
            S=S-1
            res += 1
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
        N = int(numbers[0])
        S = int(numbers[1])
        p = int(numbers[2])
        res = match(S,  p,  numbers[3:3+N])
        newline ='Case #{0}: {1}\n'.format(i, res)
        fw.write(newline)
        i=i+1
finally:
    if fr!=None:
        fr.close()
    if fw!=None:
        fw.close()
