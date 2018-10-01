import sys


def flip(S, K):
    flips = 0
    for i in range(0, len(S)-K+1):
        if S[i]=='-':
            flips += 1
            for j in range(i, i+K):
                S[j] = '+' if S[j]=='-' else '-'

    for i in range(0, len(S)):
        if S[i]=='-': return "IMPOSSIBLE"

    return flips         


fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

T = int(fin.readline())

for t in range(T):
    l = fin.readline()
    S = list(l.split()[0])
    K = int(l.split()[1])


    fout.write("Case #%i: %s\n" % (t+1, flip(S,K)))

