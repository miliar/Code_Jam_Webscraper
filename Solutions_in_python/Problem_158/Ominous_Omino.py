'''
Created on 12 Apr 2015

@author: Toby
'''

with open("D-small-attempt0.in", "r") as fin:
    filein = fin.read().splitlines()
times = int(filein.pop(0))
case = 1
with open("output2.in", "w") as fout:
    for things in filein:
        winner = False
        bit = things.split()
        x=int(bit[0])
        r=int(bit[1])
        c=int(bit[2])
        if r>c:
            temp = r
            r = c
            c = temp
        area = r*c
        if x == 1: winner = False
        elif (x>=7)|(area%x != 0)|(((x - 1) / 2) + 1 > r): winner = True
        else: winner = ((x > 2) & ((x / 2) >= r))
        answer=""
        if winner == True: answer = "Richard"
        else: answer = "Gabriel"
        fout.write("Case #%s: %s\n" % (case, answer))
        case+=1