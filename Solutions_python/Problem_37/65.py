import sys

T = int(raw_input())

all_chars = "0123456789abcdefghijklmnopqrstuvwxyz !\"#$%&'()*+,./:;<=>?@[\]^_`{|}~"
reverse_chars = ( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 37, 38, 39, 40, 41,
    42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 52,
    53, 54, 55, 56, 57, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 59, 60, 61, 62, 63, 64, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    33, 34, 35, 65, 66, 67, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )

def to_num(number, base):
    if base > 70:
        return
    result = 0L
    reversed_str = number[::-1]

    if len(number) == 0:
        return 0

    for i in range(len(reversed_str)):
        val = reverse_chars[ord(reversed_str[i])]
        result += val * (pow(base, i))

    if number[0] == '-':
        result = 0 - result

    return result

def from_num(number, base):
    if base > 70:
        return

    result = ""
    v = number
    r = 0

    if number < 0:
        v = 0 - v

    while v:
        r = v % base
        v /= base
        result += all_chars[r]

    if number < 0:
        result += "-"

    return result[::-1]

def calc(N,base):    
    if N in cur_base:
        return None
    cur_base.append(N)
    num = from_num(N,base)
    k = 0
    for c in num:
        k+= int(c)*int(c)
    if k == N:
        return k
    return calc(k,base)

for x in xrange(1,T+1):
    arr = [ int(temp) for temp in raw_input().split(' ')]
    N = 1
    while (500):
        found = True       
        N+=1   
        for base in arr:
            cur_base = []
            if calc(N,base) != 1:
                found = False
                break
        if found:
            break
    print "Case #"+str(x)+": "+str(N) 
