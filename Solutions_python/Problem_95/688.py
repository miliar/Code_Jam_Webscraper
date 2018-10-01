t=int(raw_input())

def f(s):
    if s == "a": return "y"
    elif s == "n": return "b"
    elif s == "f": return "c"
    elif s == "i": return "d"
    elif s == "c": return "e"
    elif s == "w": return "f"
    elif s == "l": return "g"
    elif s == "b": return "h"
    elif s == "k": return "i"
    elif s == "u": return "j"
    elif s == "o": return "k"
    elif s == "m": return "l"
    elif s == "x": return "m"
    elif s == "s": return "n"
    elif s == "e": return "o"
    elif s == "v": return "p"
    elif s == "z": return "q"
    elif s == "p": return "r"
    elif s == "d": return "s"
    elif s == "r": return "t"
    elif s == "j": return "u"
    elif s == "g": return "v"
    elif s == "t": return "w"
    elif s == "h": return "x"
    elif s == "y": return "a"
    elif s == "q": return "z"
    elif s == " ": return " "
    else: return "oh no"

for i in range(0,t):
    G=raw_input()
    output = "Case #" + str(i+1) + ": "
    for c in G:
    	output += f(c)
    print output

