
dictionary = {"a": "y", "b": "h", "c": "e", "d": "s", "e": "o", "f": "c", "g": "v", "h": "x", "i": "d", "j": "u", "k": "i", "l": "g", "m": "l", "n": "b", "o": "k", "p": "r", "q": "z", "r": "t", "s": "n", "t": "w", "u": "j", "v": "p", "w": "f", "x": "m", "y": "a", "z": "q", " ": " "}

lines = int(raw_input())
for i in range(lines):
    googlerese = raw_input()
    decoded = ""
    for char in googlerese:
        decoded = decoded + dictionary[char]
    print "Case #" + str(i+1) + ": " + decoded
