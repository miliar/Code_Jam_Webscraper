#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="google code jam stalls")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open(args.inputfile + ".out", "w")


def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        N, K = f.readline().split(" ")
        yield int(N), int(K)


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)


def Ls(stalls, s):
    L = 0
    for i in range(s-1,0,-1):
        if stalls[i] == 0:
            L += 1
        else:
            break
    return L

def Rs(stalls, s):
    R = 0
    for i in range(s+1,len(stalls)):
        if stalls[i] == 0:
            R += 1
        else:
            break
    return R


def beststall(stalls):
    maxs = 0
    mins = 0
    spacings = {}
    for j in range(1,len(stalls)):
        if stalls[j] == 1:
            continue
        spacing = (Ls(stalls,j), Rs(stalls,j))
        spacings[j] = spacing
        maxs = max(max(spacing),maxs)
        mins = max(min(spacing),mins)
    # print(spacings)
    # print({k: max(s) for k,s in spacings.items()})
    # print({k: min(s) for k,s in spacings.items()})
    # print( maxs)
    # print( mins)
    minmax = {k: s for k,s in spacings.items() if min(s) == mins}
    # print(minmax)
    bestmax = max([max(s) for s in minmax.values()])
    # print("bestmax",bestmax)
    for k, s in minmax.items():
        if max(s) == bestmax:
            return k, s


def solve(case):
    N, K = case
    stalls = [0 for i in range(N+2)]
    stalls[0] = stalls[-1] = 1

    if N == K:
        return (0,0)

    # print(stalls)
    while K > 0:
        S, LR = beststall(stalls)
        # print("S",S)
        stalls[S] = 1
        K -= 1
    # print(stalls)
    # print(LR)
    return max(LR), min(LR)

def main():
    for n, case in enumerate(read_input(), start=1):

        x,y = solve(case)
        answer = "{} {}".format(x,y)
        output(n, answer)


if __name__ == "__main__":
    main()
