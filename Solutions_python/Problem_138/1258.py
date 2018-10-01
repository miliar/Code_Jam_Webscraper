#! /usr/bin/env python

import sys

class Game(object):
    def __init__(self, N, n_blocks, k_blocks):
        self.N = N
        self.n_blocks = n_blocks
        self.k_blocks = k_blocks

    def cheat(self):
        # Ken plays lowest block that is greater than Naomi's
        # If Ken cannot beat Naomi he plays his lightest block
        # Naomi knows Kens blocks and cheats:
        # Pick the lowest block, say that it's == Kens highest block - 0.000001
        # Ken plays highest block and wins
        # Repeat until Naomi can win all remaining rounds: 
        # All of her blocks weigh more than kens, she picks the lightest and says
        # it's heavier than his heaviest
        

        n_points = 0
        nbs = sorted(self.n_blocks, key = lambda x: -x)
        kbs = sorted(self.k_blocks)

        for i in range(self.N):

            if all([nbs[j] > kbs[0] for j in range(len(nbs))]):
                nbt = kbs[-1] + (0.000001 * (len(nbs)+1))
                nb = nbs.pop()
            else:
                nb = nbs.pop()
                nbt = kbs[-1] - 0.000001

            kb = None
            for i in range(len(kbs)):
                if kbs[i] > nbt:
                    kb = kbs.pop(i)
                    break
            else:
                kb = kbs.pop(0)
            if nb > kb:
                n_points += 1
        return n_points

    def fair(self):
        # Naomi play in order of decreasing weight
        # Ken plays lowest block that is greater than Naomi's
        # If Ken cannot beat Naomi he plays his lightest block
        n_points = 0
        nbs = sorted(self.n_blocks)
        kbs = sorted(self.k_blocks)
        for i in range(self.N):
            nb = nbs.pop()

            kb = None
            for i in range(len(kbs)):
                if kbs[i] > nb:
                    kb = kbs.pop(i)
                    break
            else:
                kb = kbs.pop(0)
            if nb > kb:
                n_points += 1
        return n_points

if __name__ == '__main__':
    with open(sys.argv[1]) as testfile:
        t = int(testfile.readline())
        for i in range(1, t+1):
            N = int(testfile.readline())
            n_blocks = [float(x) for x in testfile.readline().split()]
            k_blocks = [float(x) for x in testfile.readline().split()]
            g1 = Game(N, n_blocks, k_blocks)
            print "Case #{}: {} {}".format(
                i,
                Game(N, n_blocks, k_blocks).cheat(),
                Game(N, n_blocks, k_blocks).fair()
            )
