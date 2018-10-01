#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="google code jam practice all your base")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open(args.inputfile + ".out", "w")

def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        N, M = (int(i) for i in f.readline().split(" "))
        print(N,M)
        lawn = []
        for i in range(N):
            lawn.append([int(c) for c in f.readline().strip().replace(" ","")])
        yield N,M,lawn


def output(n,s):
    outstring = "Case #{}: {}\n".format(n+1, s)
    print(outstring, end="")
    outfile.write(outstring)

def impossible(N, M, lawn):
    for i in range(N):
        for j in range(M):
            elm = lawn[i][j]
            if elm == max(lawn[i]):
                continue
            if elm != max([row[j] for row in lawn]):
                return True
    return False

def main():
    for n,case in enumerate(read_input()):
        # print(case)
        N,M,lawn = case
        outstring = "YES"
        if impossible(N,M,lawn):
            outstring = "NO"

        output(n,outstring)

if __name__ == "__main__":
    main()
