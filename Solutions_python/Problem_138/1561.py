#!/usr/bin/python

def main():
    fin = open('D-large.in', 'r')
    fout = open('war.out', 'w')
    
    fin.seek(0)
    ncases = int(fin.readline())
    for case in range(1, ncases + 1):
        numblocks = int(fin.readline().strip())
        naomi = sorted([float(b) for b in fin.readline().strip().split()],
                       key = lambda mass: -mass)
        ken = sorted([float(b) for b in fin.readline().strip().split()]) 
        warpoints = playWar(naomi, ken)
        cheatpoints = playCheat(naomi, ken)
        fout.write("Case #{0}: {1} {2}\n".format(case, cheatpoints, warpoints))

def playWar(naomi, ken):
    # In this case, Ken essentially has all of the knowledge
    # So Ken is playing blocks against Naomi's choices
    # The optimal strategy for Ken is to play the smallest
    # block which is greater than Naomi's choice,
    # or if there is none, the smallest block
    # Naomi can minimize the loss by playing from the largest
    # block to the smallest
    points = 0
    for nb in naomi:
        if nb > ken[-1]:
            points += 1
            ken = ken[1:]
        else:
            ken = ken[:-1]
    return points

def playCheat(naomi, ken):
    # In this case, the situation is essentially reversed
    # Naomi has all of the knowledge, and can force
    # Ken to play larger blocks than normal.
    # The optimal strategy here is for Naomi to play
    # blocks which are larger than Ken's blocks, or
    # to play the smallest block and force Ken to play
    # the largest block.
    points = 0
    for kb in reversed(ken):
        if naomi[0] > kb:
            points += 1
            naomi = naomi[1:]
        else:
            naomi = naomi[:-1]
    return points

if __name__ == "__main__":
    main()
