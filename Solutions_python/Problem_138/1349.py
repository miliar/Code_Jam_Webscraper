from math import sqrt, pow, log, ceil, log10
from sys import stdin, setrecursionlimit
import random

T = int(stdin.readline())
setrecursionlimit(1500)

def war(naomi, ken, N):
    if len(naomi) == 0:
        return 0

    if len(naomi) == 1:
        if naomi[0] > ken[0]:
            return 1
        else:
            return 0

    # Naomi choose one piece, ken choose just upper (and it does it, it does not wait to use this piece later, it can't be good for him, eg
    # if all Naomi's other pieces are larger)
    ans = 0

    nken = N - 1
    
    for invnnaomi in range(0, N):

        nnaomi = N - 1 - invnnaomi

        if (ken[nken] > naomi[nnaomi]):
            # point for ken
            nken = nken - 1
        else:            
            # point for naomi, ken keeps the good piece
            ans = ans + 1

    return ans

def deceitfulwar(naomi, ken, N):
    if len(naomi) == 0:
        return 0

    if len(naomi) == 1:
        if naomi[0] > ken[0]:
            return 1
        else:
            return 0

    # Naomi choose one small piece and says that it has a weight just below ken largest pieces, 
    # ken choose just upper (and it does it, it does not wait to use this piece later, it can't be good for him, eg
    # if all Naomi's other pieces are larger)

    # Naomi uses its large pieces
    # Then, her small, saying that they are quite large, until Naomi has a larger piece
    # And so on

    # Naomi knows that if she says something large, ken will use its smallest piece
    # so, she can lie as long as her piece is larger than ken's larger one

    # Naomi says something larger than ken largest one, and in fact, use its smallest piece which is larger than ken smallest one
    # until she has no more piece: then she says the truth
    ans = 0

    for i in range(1, N+1):
        possiblenaomi = [x for x in naomi if x > ken[0]]

        if len(possiblenaomi) >= 1:

            # lie and point for naomi
            naomi = [x for x in naomi if x != possiblenaomi[0]]
            ken = [x for x in ken if x != ken[0]]
            ans += 1

    return ans

for i in range(1, T+1):

    N, = map(int, stdin.readline().split())
    
    naomi = map(float, stdin.readline().split())
    ken = map(float, stdin.readline().split())

    naomi.sort()
    ken.sort()

    # print "inputs:"
    # print N
    # print naomi
    # print ken
    # print

    print "Case #" + str(i) + ": " + str(deceitfulwar(naomi, ken, N)) + " " + str(war(naomi, ken, N))




