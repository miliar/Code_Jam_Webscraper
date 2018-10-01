#! /usr/bin/python3

def readint(): return int(input())
def readarray(f): return map(f, input().split())

def solve(acs, ajs):
    if len(acs) == 2:
        a = (acs[0][1] - acs[1][0]) % 1440
        b = (acs[1][1] - acs[0][0]) % 1440
        if min(a, b) <= 720:
            return 2
        else:
            return 4
    elif len(ajs) == 2:
        a = (ajs[0][1] - ajs[1][0]) % 1440
        b = (ajs[1][1] - ajs[0][0]) % 1440
        if min(a, b) <= 720:
            return 2
        else:
            return 4
    else:
        return 2

_cases = readint()
for _case in range(_cases):
    ac, aj = list(readarray(int))
    acs = []
    for _ in range(ac):
        acs.append(list(readarray(int)))
    ajs = []
    for _ in range(aj):
        ajs.append(list(readarray(int)))
    
    print("Case #" + str(_case+1) + ":", solve(acs, ajs))

