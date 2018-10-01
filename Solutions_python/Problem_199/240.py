infilecode = "ALI"

import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = os.path.join(dir_path, "".join(mapping[c] for c in infilecode))
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')
T = int(input())

#def check(pattern)
for case in range(1,T+1):
    S, K = input().split()
    K = int(K)
    S = list(S)

    print(S, K)
    n = 0
    for i in range(len(S) - K + 1):
        if S[i] == "-":
            n += 1
            for j in range(K):
                if S[i+j] == "-":
                    S[i+j] = "+"
                else:
                    S[i+j] = "-"
    answer = n
    for c in S:
        if c == "-":
            answer = "IMPOSSIBLE"


    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)
    print(" ")

output.close()
