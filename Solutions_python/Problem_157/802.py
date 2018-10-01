import numpy as np



table = np.array([["1", "i", "j", "k", "U", "I", "J", "K"],
                ["i", "U", "k", "J", "I", "1", "K", "j"],
                ["j", "K", "U", "i", "J", "k", "1", "I"],
                ["k", "j", "I", "U", "K", "J", "i", "1"],
                ["U", "I", "J", "K", "1", "i", "j", "k"],
                ["I", "1", "K", "j", "i", "U", "k", "J"],
                ["J", "k", "1", "I", "j", "K", "U", "i"],
                ["K", "J", "i", "1", "k", "j", "I", "U"]])

def mult(a,b):
    d = {'1': 0,'i': 1, 'j' : 2, 'k': 3, 'U' : 4, 'I' : 5, 'J': 6, 'K' : 7 }
    res = table[d[a], d[b]]
    return res

def valid(l, t):
    w = ''.join(l)
    if(len(w) < 3):
        print("Case #{0}: NO".format(t+1))
        return 0

    return 1

T = int(raw_input())

for t in range(T):
    line = raw_input()
    L, X = line.split()
    L = int(L)
    X = int(X)
    s = raw_input()
    patt = ["i","j","k"]

    word = s*X
    red = list(word)

    if(not valid(red, t)):
        continue

    for i in range(3):
        while(red[i] != patt[i] and len(red) > 3):
            red[i] = mult(red[i], red[i+1])
            red.pop(i+1)

        if(not valid(red, t)):
            break

    while(len(red) > 3):
        red[2] = mult(red[2], red[3])
        red.pop(3)


    w = ''.join(red)
    #print("END{0}: {1}".format(t+1, red))
    if(w == "ijk"):
        print("Case #{0}: YES".format(t+1))
    else:
        print("Case #{0}: NO".format(t+1))
