import sys

T = int(sys.stdin.readline())

maping = {"q": "z", "z": "q", "e": "o", "j": "u", "p": "r", 
        "m": "l", "y": "a", "s": "n", "l": "g", "c": "e", 
        "k": "i", "d": "s", "x": "m", "v": "p", "n": "b", 
        "r": "t", "i": "d", "b": "h", "t": "w", "a": "y", 
        "h": "x", "w": "f", "f": "c", "o": "k", "u": "j", "g": "v"}

for case in range(1, T + 1) :
    output = "Case #" + str(case) + ": "
    line = sys.stdin.readline().strip()
    for c in line:
        if c in maping:
            output += maping[c]
        else:
            output += c
    print output

