import math


def calc(stall, people):
    rep = 2**(len(bin(people))-3)
    shift = people-1
    num = math.ceil((stall-shift) / rep)-1
    return num // 2 + num % 2, num//2


ff = 'C-small-2-attempt0'
with open(ff+'.in') as fi, open(ff+'.out', 'w') as fo:
    cases = int(fi.readline())
    for t in range(cases):
        stall, people = fi.readline().split(' ')
        stall, people = int(stall), int(people)
        # print(stall, people)
        mx, mn = calc(stall, people)
        fo.writelines('Case #{}: {} {}'.format(t+1, mx, mn)+'\n')
        # break
