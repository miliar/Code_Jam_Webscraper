# Code Jam Round 1C - Prob C
# 13/9/2009

import random

inname = 'E:\C.in.txt'

fin = open(inname, 'r')
fout = open('E:\C.out.txt', 'w')

lines = fin.readlines()

cases = int(lines[0].strip())

def factorial(n):
    i = 1
    for j in range(2, n+1):
        i *= j
    return i

# brute to do it quickly (cause Q <= 5)

for case in range(1, cases + 1):
    (P, Q) = lines[((case - 1) * 2) + 1].strip().split()
    P = int(P)
    Q = int(Q)
    R = [int(x) for x in lines[((case - 1)*2) + 2].strip().split()]

    min_value = P*Q

    used = set()

    while len(used) < factorial(Q):
        trial = list(R)
        random.shuffle(trial)
        trial_s = 'm'.join([str(i) for i in trial])
        if not trial_s in used:
            used.add(trial_s)
            cells = [1]*P
            bribe = 0
            for release in trial:
                cells[release-1] = 0
                new_bribe = 0
                for k in range(release, P):
                    if cells[k] == 1:
                        new_bribe += 1
                    else:
                        break
                for k in range(release - 2, -1, -1):
                    if cells[k] == 1:
                        new_bribe += 1
                    else:
                        break
                bribe += new_bribe
            min_value = min(min_value, bribe)
    print(case)
    fout.write('Case #' + str(case) + ': ' + str(min_value) + '\n')
        
fout.close()
fin.close()   
    
