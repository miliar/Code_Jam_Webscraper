#!/usr/bin/env python3

def test_case():
    AC, AJ = (int(x) for x in input().split())
    TC = []
    TJ = []

    for i in range(AC):
        a = [int(x) for x in input().split()]
        TC.append(a)
    for i in range(AJ):
        a = [int(x) for x in input().split()]
        TJ.append(a)
    


    chrono = {}
    sss = {}
    sss['C'] = 0
    sss['J'] = 0

    for a in TC:
        chrono[a[0]] = ('C', a[0], a[1])
        sss['C'] += a[1] - a[0]
    for a in TJ:
        chrono[a[0]] = ('J', a[0], a[1])
        sss['J'] += a[1] - a[0]

    
    cont = {'C': [], 'J': []}
    change = []

    chrono = [chrono[x] for x in sorted(chrono)]

    ret = 0

    for (prev, this) in zip(chrono, chrono[1:]):
        time = this[1] - prev[2]
        if prev[0] == this[0]:
            cont[prev[0]].append(time)
        else:
            change.append(time)
            ret += 1

    time = chrono[0][1] + 24 * 60 - chrono[-1][2]
    if chrono[-1][0] != chrono[0][0]:
        ret += 1
        change.append(time)
    else:
        cont[chrono[-1][0]].append(time)


#    print("change: ", change)
#    print("cont:   ", cont)
#    print("sumC: ", sss['C'], " sumJ: ", sss['J'])

    def all_sum(x):
        return sss[x] + sum(cont[x])

#    print("C: ", sss['C'] + sum(cont['C']), " -- J: ", sss['J'] + sum(cont['J']))


    gt = 'C' if all_sum('C') > all_sum('J') else 'J'
    if all_sum(gt) > 720:
#        print("ERROR")
        if all_sum(gt) - sum(change) > 720: # no quick fix!
#            print("NO QUIOC FIX\n")
            new = reversed(sorted(cont[gt]))

            to_go = all_sum(gt) - sum(change) - 720
            compensation = 0
            for comp in new:
                compensation += comp
                ret += 2
                if compensation >= to_go:
                   break 


                # TODO przypadek jak AC + AJ == 0???
    return ret

T = int(input())

for t in range(1, T+1):
    ret = test_case()
    print("Case #{}: {}".format(t, ret))
