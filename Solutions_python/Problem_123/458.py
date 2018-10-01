from sys import stdin

def edible_len(A, sequence):
    if len(sequence) == 0:
        return 0
    elif A > sequence[0]:
        return 1 + edible_len(A + sequence[0], sequence[1:])
    else:
        return 0


def main():
    for case in range(1, int(stdin.readline()) + 1):
        A, N = map(int, stdin.readline().split())
        motes = map(int, stdin.readline().split())
        motes.sort()
        ops = 0
        Adding = 0

        while len(motes) > 0:
            # consume as many as possible
            while len(motes) > 0 and A > motes[0]:
                A += motes[0]
                motes.remove(motes[0])

            if len(motes) > 1 and Adding == 0:
                appends = 0
                bestlen = 0
                bestappends = 0
                An = A
                for i in range(len(motes)):
                    An += An - 1
                    appends +=1
                    if edible_len(An, motes)-appends > bestlen-bestappends:
                        bestlen = edible_len(An, motes)
                        bestappends = appends
                if bestlen - bestappends >= 1:
                    Adding = bestappends

            if len(motes) == 0:
                pass
            # if you can add one to reach the gap, add greedily
            elif len(motes) > 1 and Adding > 0:
                    ops += 1
                    motes.insert(0,A-1)
                    Adding -= 1
            # if you have to delete the last one, or everyone else, do so
            else:
                ops += 1
                motes.remove(motes[0])
                if len(motes) == 0:
                    break

        print "Case #" + str(case) + ": " + str(ops)

if __name__=="__main__":
    main()
