import copy
import sys

rdLn = sys.stdin.readline

def readInt():
    return int(rdLn()[:-1])

def readNums():
    return map(float,(rdLn()[:-1]).split(' '))

T = readInt()

def kensMove(moveN, kens):
    if (moveN > kens[-1]):
        return 0
    i = len(kens) - 1
    while (i >= 0 and kens[i] > moveN):
        i -= 1
    return i+1

def playWar(n, naomis, kens):
    score = 0
    # Naomi will just play her peices in reverse order
    for i in range(n-1, -1, -1):
        moveN = naomis.pop(i)
        # Ken will respond with his best move
        moveK = kens.pop(kensMove(moveN, kens))
        # if Naomi's move wins, she gets a point
        if (moveN > moveK):
            score += 1
    # return Naomi's score
    return score

epsilon = 0.0000001

# returns tuple (moveN, tellN)
def naomisMove(naomis, kens):
    if (naomis[0] < kens[0]): # burn Naomi's useless blocks for Ken's hightest
        return (naomis.pop(0), kens[-1]-epsilon)
    else: # else, get Ken to burn his lowest, and Naomi still wins the round
        return (naomis.pop(0), 1)

def playDWar(n, naomis, kens):
    score = 0
    for i in range(0, n):
        # Naomi plays her best move
        (moveN, tellN) = naomisMove(naomis, kens)
        # Ken will respond with his best move
        moveK = kens.pop(kensMove(tellN, kens))
        # if Naomi's move wins, she gets a point
        if (moveN > moveK):
            score += 1
    # return Naomi's score 
    return score

# actual program
for i in range(1, T+1):
    n = readInt()
    naomis = sorted(readNums())
    kens = sorted(readNums())

    n2 = copy.deepcopy(naomis)
    k2 = copy.deepcopy(kens)

    wScore = playWar(n, naomis, kens)
    dwScore = playDWar(n, n2, k2)

    print "Case #{0}: {1} {2}".format(i,dwScore,wScore)
