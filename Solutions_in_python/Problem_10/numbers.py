#!/usr/bin/python

def solve(P,K,L, freqs):
    keys = [ [] for i in range(K)]
    freqs_with_index = [(i, freqs[i]) for i in range(len(freqs))]
    freqs_with_index.sort( lambda x,y : cmp(y[1], x[1]) )

    c = 0
    while len(freqs_with_index) != 0:
        for i in range(len(keys)):
            if len(freqs_with_index) == 0:
                break
            if len(keys[i]) < P:
                keys[i].append(freqs_with_index[0][0])
                c = c + ((len(keys[i]) ) * freqs_with_index[0][1])
                del freqs_with_index[0]

    return c




N = int(raw_input())
for i in range(N):
    P, K, L = [int(x) for x in raw_input().split(" ")]
    freqs   = [int(x) for x in raw_input().split(" ")]
    assert len(freqs) == L;

    print "Case #%i: %s" %(i+1, solve(P,K,L, freqs));
